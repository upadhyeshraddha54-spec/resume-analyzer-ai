from docx import Document
from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import os
import requests

app = Flask(__name__)

# Skills list
skills = [
    "Python", "Java", "SQL", "Machine Learning", "HTML", "CSS", "JavaScript",
    "React", "Node.js", "Django", "Spring Boot", "Kotlin", "Android SDK",
    "Linux", "Docker", "Kubernetes", "CI/CD", "AWS", "Pandas", "NumPy", "Firebase", "Statistics"
]

# Job roles
job_skills = {
    "data_scientist": ["Python", "SQL", "Machine Learning", "Pandas", "NumPy", "Statistics"],
    "web_developer": ["HTML", "CSS", "JavaScript", "React", "Node.js"],
    "backend_developer": ["Python", "Java", "SQL", "APIs", "Django", "Spring Boot"],
    "android_developer": ["Java", "Kotlin", "Android SDK", "Firebase"],
    "devops_engineer": ["Linux", "Docker", "Kubernetes", "CI/CD", "AWS"]
}

# -------- Extract Resume Text --------
def extract_resume_text(file):
    text = ""

    if file.filename.endswith(".pdf"):
        reader = PdfReader(file)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + " "

    elif file.filename.endswith(".docx"):
        doc = Document(file)
        for para in doc.paragraphs:
            text += para.text + " "

    else:
        file_content = file.read()
        try:
            text = file_content.decode("utf-8")
        except:
            text = file_content.decode("latin-1")

    return text.lower().strip()


# -------- Skill Matching --------
def match_skills(resume_text, required_skills):
    matched = [s for s in required_skills if s.lower() in resume_text]
    missing = [s for s in required_skills if s not in matched]
    score = (len(matched) / len(required_skills)) * 100 if required_skills else 0
    return matched, missing, round(score, 2)


# -------- Role Prediction --------
def predict_role(resume_text):
    scores = {}
    for role, skill_list in job_skills.items():
        match = sum(1 for s in skill_list if s.lower() in resume_text)
        scores[role] = (match / len(skill_list)) * 100 if skill_list else 0

    best_role = max(scores, key=scores.get)
    return best_role.replace("_", " ").title(), round(scores[best_role], 2)


# -------- Resume Quality --------
def resume_quality_score(resume_text, required_skills):
    matched = [s for s in required_skills if s.lower() in resume_text]
    skill_score = (len(matched) / len(required_skills)) * 100 if required_skills else 0

    word_count = len(resume_text.split())
    length_score = min(100, max(0, word_count / 10))

    sentences = resume_text.split('.')
    avg_len = sum(len(s.split()) for s in sentences) / (len(sentences) + 1)
    readability = max(0, 100 - abs(avg_len - 20) * 5)

    final = round(0.5 * skill_score + 0.3 * length_score + 0.2 * readability, 2)
    return final


# -------- AI Analysis (OpenRouter) --------


def ai_resume_analysis(resume_text, job_role):

    resume_text = resume_text[:1200]

    prompt = f"""
    Analyze this resume for {job_role}.
    Give strengths, missing skills, and improvements in bullet points.
    Resume:
    {resume_text}
    """

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        data = response.json()
        print("DEBUG RESPONSE:", data)  # 👈 VERY IMPORTANT

        # ✅ Case 1: proper response
        if "choices" in data:
            return data["choices"][0]["message"]["content"]

        # ❌ Case 2: error from API
        if "error" in data:
            return f"API Error: {data['error']}"

        # ❌ Case 3: unknown format
        return f"Unexpected response: {data}"

    except Exception as e:
        return f"System Error: {str(e)}"
# -------- Flask Route --------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files["resume"]
        role = request.form["role"]

        if file:
            text = extract_resume_text(file)
            required = job_skills.get(role, [])

            matched, missing, score = match_skills(text, required)
            predicted_role, predicted_score = predict_role(text)
            quality = resume_quality_score(text, required)
            ai_feedback = ai_resume_analysis(text, role)

            result = {
                "matched": matched,
                "missing": missing,
                "skill_score": score,
                "predicted_role": predicted_role,
                "predicted_score": predicted_score,
                "quality_score": quality,
                "ai_feedback": ai_feedback
            }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)