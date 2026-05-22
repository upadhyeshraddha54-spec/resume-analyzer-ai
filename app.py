from docx import Document
from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import requests
import re

app = Flask(__name__)

# ---------------- API KEY ----------------
from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# ---------------- Skills ----------------
skills = [
    "Python", "Java", "SQL", "Machine Learning",
    "HTML", "CSS", "JavaScript", "React",
    "Node.js", "Django", "Spring Boot",
    "Kotlin", "Android SDK", "Linux",
    "Docker", "Kubernetes", "CI/CD",
    "AWS", "Pandas", "NumPy",
    "Firebase", "Statistics"
]

# ---------------- Job Roles ----------------
job_skills = {

    "data_scientist": [
        "Python",
        "SQL",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "Statistics"
    ],

    "web_developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js"
    ],

    "backend_developer": [
        "Python",
        "Java",
        "SQL",
        "API",
        "Django",
        "Spring Boot"
    ],

    "android_developer": [
        "Java",
        "Kotlin",
        "Android SDK",
        "Firebase"
    ],

    "devops_engineer": [
        "Linux",
        "Docker",
        "Kubernetes",
        "CI/CD",
        "AWS"
    ]
}

# ---------------- Extract Resume Text ----------------
def extract_resume_text(file):

    text = ""

    try:

        # PDF
        if file.filename.endswith(".pdf"):

            reader = PdfReader(file)

            for page in reader.pages:

                content = page.extract_text()

                if content:
                    text += content + " "

        # DOCX
        elif file.filename.endswith(".docx"):

            doc = Document(file)

            for para in doc.paragraphs:
                text += para.text + " "

        # TXT
        else:

            file_content = file.read()

            try:
                text = file_content.decode("utf-8")

            except:
                text = file_content.decode("latin-1")

    except Exception as e:
        print("Resume Extraction Error:", e)

    # Clean spaces
    text = re.sub(r"\s+", " ", text)

    return text.lower().strip()

# ---------------- Skill Matching ----------------
def match_skills(resume_text, required_skills):

    resume_text = resume_text.lower()

    matched = []

    for skill in required_skills:

        if skill.lower() in resume_text:
            matched.append(skill)

    missing = [
        skill for skill in required_skills
        if skill not in matched
    ]

    score = (
        len(matched) / len(required_skills)
    ) * 100 if required_skills else 0

    return matched, missing, round(score, 2)

# ---------------- Role Prediction ----------------
def predict_role(resume_text):

    resume_text = resume_text.lower()

    scores = {}

    for role, skill_list in job_skills.items():

        matched = sum(
            1 for skill in skill_list
            if skill.lower() in resume_text
        )

        score = (
            matched / len(skill_list)
        ) * 100 if skill_list else 0

        scores[role] = round(score, 2)

    best_role = max(scores, key=scores.get)

    return (
        best_role.replace("_", " ").title(),
        scores[best_role],
        scores
    )

# ---------------- ATS SCORE ----------------
def ats_score(resume_text, required_skills):

    resume_text = resume_text.lower()

    score = 30

    # ---------------- Skill Matching ----------------
    matched_skills = [
        skill for skill in required_skills
        if skill.lower() in resume_text
    ]

    skill_percent = (
        len(matched_skills) / len(required_skills)
    ) * 100 if required_skills else 0

    score += skill_percent * 0.35

    # ---------------- Important Sections ----------------
    sections = [
        "skills",
        "projects",
        "education",
        "experience"
    ]

    found_sections = sum(
        1 for section in sections
        if section in resume_text
    )

    section_score = (
        found_sections / len(sections)
    ) * 20

    score += section_score

    # ---------------- Resume Length ----------------
    word_count = len(resume_text.split())

    if word_count >= 400:
        score += 10

    elif word_count >= 250:
        score += 5

    # ---------------- Portfolio Links ----------------
    if "github" in resume_text:
        score += 5

    if "linkedin" in resume_text:
        score += 5

    # ---------------- Action Words ----------------
    strong_words = [
        "developed",
        "built",
        "implemented",
        "created",
        "optimized",
        "designed",
        "improved",
        "managed"
    ]

    action_count = sum(
        1 for word in strong_words
        if word in resume_text
    )

    score += min(action_count * 2, 10)

    # ---------------- Certifications ----------------
    if "certification" in resume_text:
        score += 5

    # ---------------- Internship ----------------
    if "internship" in resume_text:
        score += 5

    return round(min(score, 100), 2)

# ---------------- RESUME QUALITY SCORE ----------------
def resume_quality_score(resume_text, required_skills):

    resume_text = resume_text.lower()

    score = 40

    # ---------------- Skill Relevance ----------------
    matched_skills = [
        skill for skill in required_skills
        if skill.lower() in resume_text
    ]

    skill_score = (
        len(matched_skills) / len(required_skills)
    ) * 30 if required_skills else 0

    score += skill_score

    # ---------------- Projects ----------------
    if "project" in resume_text:
        score += 10

    # ---------------- Experience ----------------
    if "experience" in resume_text:
        score += 10

    # ---------------- GitHub ----------------
    if "github" in resume_text:
        score += 5

    # ---------------- LinkedIn ----------------
    if "linkedin" in resume_text:
        score += 5

    # ---------------- Resume Length ----------------
    word_count = len(resume_text.split())

    if word_count >= 400:
        score += 10

    elif word_count >= 250:
        score += 5

    # ---------------- Achievement Keywords ----------------
    achievement_words = [
        "%",
        "improved",
        "increased",
        "reduced",
        "accuracy",
        "optimized",
        "developed",
        "deployed"
    ]

    achievement_count = sum(
        1 for word in achievement_words
        if word in resume_text
    )

    score += min(achievement_count * 2, 10)

    # ---------------- Education ----------------
    if "education" in resume_text:
        score += 5

    # ---------------- Certifications ----------------
    if "certification" in resume_text:
        score += 5

    return round(min(score, 100), 2)

# ---------------- ATS Suggestions ----------------
def ats_suggestions(resume_text, missing_skills):

    suggestions = []

    if len(resume_text.split()) < 350:
        suggestions.append(
            "Increase resume content with projects and measurable achievements."
        )

    if missing_skills:
        suggestions.append(
            "Add missing technical skills relevant to the target role."
        )

    if "project" not in resume_text:
        suggestions.append(
            "Add a dedicated projects section."
        )

    if "github" not in resume_text:
        suggestions.append(
            "Include GitHub or portfolio links."
        )

    if "experience" not in resume_text:
        suggestions.append(
            "Add internship or practical experience."
        )

    return suggestions

# ---------------- Keyword Frequency ----------------
def keyword_frequency(resume_text):

    labels = []
    values = []

    for skill in skills:

        count = resume_text.count(skill.lower())

        if count > 0:
            labels.append(skill)
            values.append(count)

    return labels, values

# ---------------- Learning Roadmap ----------------
def learning_roadmap(role, missing_skills):

    roadmap = []

    for skill in missing_skills:

        roadmap.append(
            f"Learn {skill} through projects and online courses."
        )

    if role == "data_scientist":

        roadmap.append(
            "Build Machine Learning projects using Scikit-learn and Pandas."
        )

    elif role == "web_developer":

        roadmap.append(
            "Create responsive React applications with APIs."
        )

    elif role == "backend_developer":

        roadmap.append(
            "Develop REST APIs using Flask or Django."
        )

    elif role == "android_developer":

        roadmap.append(
            "Build Android apps using Kotlin and Firebase."
        )

    elif role == "devops_engineer":

        roadmap.append(
            "Practice Docker deployment and CI/CD pipelines."
        )

    return roadmap

# ---------------- AI Resume Analysis ----------------
def ai_resume_analysis(resume_text, job_role):

    resume_text = resume_text[:2000]

    prompt = f"""
You are an expert ATS Resume Reviewer and Senior Tech Recruiter.

Analyze the resume specifically for the role: {job_role}.

RULES:
- Keep feedback concise and professional
- Avoid generic suggestions
- Give recruiter-style feedback
- Focus on ATS optimization
- Mention impactful improvements only
- Use modern hiring standards

Return response in this format:

⭐ Strengths
- point

⚠ Missing Skills
- point

🚀 Improvements
- point

📄 Resume Structure Feedback
- point

🎯 ATS Optimization Tips
- point

Resume:
{resume_text}
"""

    try:

        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:5000",
            "X-Title": "AI Resume Analyzer"
        }

        json_data = {
            "model": "openai/gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=json_data
        )

        data = response.json()

        if "choices" in data:

            return data["choices"][0]["message"]["content"]

        elif "error" in data:

            return f"API Error: {data['error']}"

        else:

            return "AI analysis unavailable."

    except Exception as e:

        return f"System Error: {str(e)}"

# ---------------- Flask Route ----------------
@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        file = request.files["resume"]

        role = request.form["role"]

        if file:

            # Extract Text
            text = extract_resume_text(file)

            # Required Skills
            required = job_skills.get(role, [])

            # Skill Match
            matched, missing, score = match_skills(
                text,
                required
            )

            # Role Prediction
            predicted_role, predicted_score, role_scores = predict_role(text)

            # Resume Quality
            quality = resume_quality_score(
                text,
                required
            )

            # ATS Score
            ats = ats_score(
                text,
                required
            )

            # Suggestions
            suggestions = ats_suggestions(
                text,
                missing
            )

            # Keywords
            keyword_labels, keyword_values = keyword_frequency(text)

            # Roadmap
            roadmap = learning_roadmap(
                role,
                missing
            )

            # AI Feedback
            ai_feedback = ai_resume_analysis(
                text,
                role
            )

            result = {
                "matched": matched,
                "missing": missing,
                "skill_score": score,
                "predicted_role": predicted_role,
                "predicted_score": predicted_score,
                "quality_score": quality,
                "ats_score": ats,
                "ats_suggestions": suggestions,
                "role_scores": role_scores,
                "keyword_labels": keyword_labels,
                "keyword_values": keyword_values,
                "roadmap": roadmap,
                "ai_feedback": ai_feedback
            }

    return render_template(
        "index.html",
        result=result
    )

# ---------------- Run Flask ----------------
if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )