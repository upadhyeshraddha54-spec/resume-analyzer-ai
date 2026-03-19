

# Resume Analyzer with LLM-Driven Insights

**Resume Analyzer with LLM-Driven Insights** is a full-stack web application that evaluates resumes, provides role-based feedback, and generates structured insights using Large Language Models (LLMs). The system helps identify skill gaps, predict suitable roles, and suggest actionable improvements for candidates.

---

##  Overview

This application simulates an automated resume screening system by combining **rule-based evaluation** with **LLM-powered analysis**. It provides:

* Skill matching for specific job roles
* Resume quality scoring
* Suggestions to improve candidate profiles

The tool is ideal for job seekers, recruiters, and HR teams looking to enhance resume evaluation efficiency.

---

##  Key Features

* 📄 **Resume Parsing:** Supports PDF & DOCX formats
* 🎯 **Role-Based Skill Matching:** Compare candidate skills with job requirements
* 📊 **Skill Match Score:** Visual progress bars for skill alignment
* 🧠 **LLM-Powered Analysis:** Generate structured insights from resumes
* 🔍 **Missing Skills Detection:** Identify skill gaps for career growth
* 💼 **Role Prediction:** Suggest suitable roles based on resume content
* 📈 **Resume Quality Scoring:** Evaluate overall resume effectiveness
* 🎨 **Responsive UI:** Clean, user-friendly interface

---

## 🛠️ Tech Stack

**Frontend**

* HTML5, CSS3

**Backend**

* Python (Flask)

**AI Integration**

* Large Language Model via OpenRouter API

**Libraries**

* PyPDF2 (PDF parsing)
* python-docx (DOCX parsing)
* requests (API calls)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-analyzer-ai.git
cd resume-analyzer-ai
```

### 2. Install Dependencies

```bash
pip install flask PyPDF2 python-docx requests
```

### 3. Configure API Key

```bash
export OPENROUTER_API_KEY="your_api_key_here"
```

### 4. Run the Application

```bash
python app.py
```

### 5. Access the App

Open your browser and go to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

##  How It Works

1. Upload your resume (PDF/DOCX).
2. Extract text from the file.
3. Match extracted skills against selected job roles.
4. Calculate:

   * **Skill Match Score**
   * **Resume Quality Score**
5. Generate structured feedback using LLM:

   * Strengths
   * Missing Skills
   * Improvement Suggestions

---

## Project Structure

```
resume-analyzer-ai/
│── app.py
│── templates/
│   └── index.html
│── static/ (optional)
│── README.md
│── .gitignore
```

---

##  Future Enhancements

* Cloud deployment (Render / AWS)
* Analytics dashboard for skill trends
* Export resume analysis as PDF
* User authentication and accounts
*  Enhanced LLM-based scoring and suggestions

---

## Project Highlights

* Combines **rule-based logic** with **LLM-driven insights**
* Provides **automated scoring** for resume quality and skill alignment
* Generates **intelligent feedback** to help candidates improve their resumes


