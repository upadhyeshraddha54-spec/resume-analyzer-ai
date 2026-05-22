# AI Resume Analyzer with LLM-Driven Insights 🚀

AI Resume Analyzer with LLM-Driven Insights is an intelligent ATS Resume Screening and Career Recommendation platform that evaluates resumes using rule-based scoring and Large Language Models (LLMs).

The application analyzes resumes, predicts suitable tech roles, calculates ATS compatibility, evaluates resume quality, detects missing skills, and generates recruiter-style AI feedback with actionable improvement suggestions.

---

# 🌟 Overview

This project simulates a modern AI-powered Applicant Tracking System (ATS) used by recruiters and hiring teams.

It combines:

* ATS-based resume evaluation
* Skill matching algorithms
* Role prediction logic
* Resume quality scoring
* LLM-powered recruiter feedback
* Interactive analytics dashboard

The platform helps candidates optimize resumes for better shortlisting and interview opportunities.

---

#  Key Features

## 📄 Resume Parsing

Supports:

* PDF resumes
* DOCX resumes
* TXT files

Extracts and processes resume content automatically.

---

##  ATS Resume Scoring

Calculates ATS compatibility based on:

* Technical skills
* Resume keywords
* Project sections
* Experience sections
* Resume formatting
* Contact details
* GitHub/portfolio presence

---

##  AI Recruiter Feedback

Uses Large Language Models through OpenRouter API to generate:

* Resume strengths
* Missing skills
* Resume improvement suggestions
* ATS optimization tips
* Structure feedback

---

## 🔍 Skill Gap Detection

Compares resume skills with industry-required skills and identifies:

* Matched skills
* Missing skills
* Skill match percentage

---

##  Role Prediction System

Predicts suitable career roles based on resume content:

* Data Scientist
* Backend Developer
* Web Developer
* Android Developer
* DevOps Engineer

---

## 📈 Resume Quality Analysis

Evaluates:

* Resume completeness
* Technical depth
* Project quality
* Achievement impact
* Readability
* ATS readiness

---

## Interactive Dashboard

Visualized using Chart.js:

* Doughnut charts
* Radar charts
* Keyword frequency graphs
* Skill match analytics

---

##  Personalized Learning Roadmap

Suggests learning paths and missing technologies based on target role requirements.

---

#  Tech Stack

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* Chart.js

## Backend

* Python
* Flask

## AI Integration

* OpenRouter API
* GPT-4o-mini

## Libraries

* PyPDF2
* python-docx
* requests
* python-dotenv
* gunicorn

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash id="l8f3m1"
git clone https://github.com/upadhyeshraddha54-spec/Resume-Analyzer-with-LLM-Driven-Insights.git
```

---

## 2️⃣ Navigate to Project Directory

```bash id="v2q9x7"
cd Resume-Analyzer-with-LLM-Driven-Insights
```

---

## 3️⃣ Create Virtual Environment

### Mac/Linux

```bash id="n7m4k2"
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash id="q5r8t1"
python -m venv .venv
.venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash id="x1k6v9"
pip install -r requirements.txt
```

---

#  Environment Variables

Create a `.env` file in the project root:

```env id="m4p7w2"
OPENROUTER_API_KEY=your_openrouter_api_key
```

Get API key from:

[OpenRouter](https://openrouter.ai/keys?utm_source=chatgpt.com)

---

# ▶️ Run Application Locally

```bash id="f9x3m5"
python app.py
```

Open browser:

```text id="u6k1r8"
http://127.0.0.1:5000
```

---

# ☁️ Deployment (Render)

This project is deployment-ready on:

* Render
* Railway
* Replit
* VPS Servers

## Render Build Command

```bash id="r2w8v4"
pip install -r requirements.txt
```

## Render Start Command

```bash id="t5m1q7"
gunicorn app:app
```

---

# 📂 Project Structure

```text id="a8n4k2"
Resume-Analyzer-with-LLM-Driven-Insights/
│
├── app.py
├── requirements.txt
├── Procfile
├── .gitignore
├── .env
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

# 📊Dashboard Analytics

The application provides:

* ATS Score
* Resume Quality Score
* Skill Match %
* Role Prediction
* Missing Skills Analysis
* Keyword Frequency Analysis
* AI Recruiter Insights

---

#  AI Feedback Includes

* Strength analysis
* Missing skill identification
* Resume improvement suggestions
* ATS optimization recommendations
* Resume structure feedback

---

#  Security Best Practices

* API keys secured using `.env`
* `.gitignore` prevents secret exposure
* GitHub secret scanning compliant
* Environment variable-based configuration

---

#  Future Enhancements

* Resume PDF export
* Job description matching
* AI-generated resume rewriting
* Authentication system
* User dashboard
* Resume history tracking
* AI mock interview system
* Cloud database integration

---

# Project Highlights

* Combines ATS logic with LLM-powered analysis
* Generates recruiter-style feedback
* Provides intelligent career recommendations
* Interactive visual analytics dashboard
* Production-ready Flask deployment

---

#  Developer

Developed by Shraddha Upadhye

GitHub:

[Shraddha Upadhye GitHub](https://github.com/upadhyeshraddha54-spec?utm_source=chatgpt.com)

---

# Support

If you found this project useful:

* Star the repository
* Fork the project
* Share it with others


