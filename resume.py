print("Select Job Role:")
print("1. Data Analyst")
print("2. Web Developer")
print("3. ML Engineer")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    job_description = "Python SQL Excel Data Analysis"
elif choice == "2":
    job_description = "HTML CSS JavaScript React"
elif choice == "3":
    job_description = "Python Machine Learning Deep Learning"
else:
    print("Invalid choice")
    exit()

# 📄 Read resume from file
with open("resume.txt", "r") as file:
    resume_text = file.read()

skills = [
    "Python", "Java", "SQL", "Machine Learning",
    "Data Analysis", "Excel", "React", "HTML", "CSS",
    "JavaScript", "Deep Learning"
]

required_skills = []
matched_skills = []

# Required skills
for skill in skills:
    if skill.lower() in job_description.lower():
        required_skills.append(skill)

# Matched skills
for skill in required_skills:
    if skill.lower() in resume_text.lower():
        matched_skills.append(skill)

# Score
if len(required_skills) > 0:
    score = (len(matched_skills) / len(required_skills)) * 100
else:
    score = 0

print("\n===== RESULT =====")
print("Required Skills:", required_skills)
print("Matched Skills:", matched_skills)
print("Match Score:", score, "%")

# Suggestions
print("\nSkills you should improve:")
for skill in required_skills:
    if skill not in matched_skills:
        print("-", skill)