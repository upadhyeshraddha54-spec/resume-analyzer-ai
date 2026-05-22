AI Resume Analyzer
An intelligent ATS resume screening platform that combines rule-based scoring with LLM-powered recruiter feedback to help candidates optimize their resumes.

Live Demo :  https://resume-analyzer-with-llm-driven-insights.onrender.com

Overview
This project simulates a modern Applicant Tracking System (ATS) used by recruiters and hiring teams. It evaluates resumes across multiple dimensions — ATS compatibility, skill gaps, role fit, and quality — then generates recruiter-style feedback using an LLM to help candidates improve their chances of being shortlisted.

Features

ATS scoring — evaluates technical skills, keywords, project sections, formatting, contact info, and GitHub presence
Role prediction — predicts suitable roles: Data Scientist, Backend Developer, Web Developer, Android Developer, or DevOps Engineer
Skill gap detection — compares resume skills against industry requirements; shows matched vs. missing skills and match percentage
Resume quality analysis — scores completeness, technical depth, project quality, achievement impact, readability, and ATS readiness
LLM recruiter feedback — generates strengths, improvement suggestions, and ATS optimization tips via OpenRouter API
Interactive dashboard — doughnut charts, radar charts, keyword frequency graphs, and skill match analytics via Chart.js
Learning roadmap — suggests learning paths and missing technologies based on target role


Tech Stack
LayerTechnologyFrontendHTML5, CSS3, Bootstrap 5, Chart.jsBackendPython, FlaskAIOpenRouter API (GPT-4o-mini)File parsingPyPDF2, python-docxDeploymentGunicorn, Render / Railway / Replit

Prerequisites

Python 3.8 or higher
pip
An OpenRouter API key


Installation
1. Clone the repository
bashgit clone https://github.com/upadhyeshraddha54-spec/Resume-Analyzer-with-LLM-Driven-Insights.git
cd Resume-Analyzer-with-LLM-Driven-Insights
2. Create and activate a virtual environment
bash# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
3. Install dependencies
bashpip install -r requirements.txt
4. Configure environment variables
Create a .env file in the project root:
envOPENROUTER_API_KEY=your_openrouter_api_key_here
5. Run the application
bashpython app.py
Open your browser at http://127.0.0.1:5000

Project Structure
Resume-Analyzer-with-LLM-Driven-Insights/
├── app.py
├── requirements.txt
├── Procfile
├── .env
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md

Deployment
This project is ready to deploy on Render, Railway, or Replit.
Render configuration:
SettingValueBuild commandpip install -r requirements.txtStart commandgunicorn app:app
Set OPENROUTER_API_KEY as an environment variable in your hosting provider's dashboard — do not commit your .env file.

Supported File Formats

PDF (.pdf)
Word documents (.docx)
Plain text (.txt)


Dashboard Output
After uploading a resume, the dashboard displays:

ATS compatibility score
Resume quality score
Skill match percentage
Predicted role
Missing skills
Keyword frequency analysis
AI recruiter insights


Roadmap

 Job description matching
 AI-generated resume rewriting
 Resume PDF export
 Authentication and user dashboard
 Resume history tracking
 AI mock interview system
 Cloud database integration


Security

API keys are stored in .env and never committed to version control
.gitignore is configured to exclude secrets
Compliant with GitHub secret scanning


Contributing
Contributions are welcome. Please open an issue first to discuss what you'd like to change, then submit a pull request.

License
This project is licensed under the MIT License.

Author
Developed by Shraddha Upadhye
If you find this project useful, consider giving it a star on GitHub.

Roadmap

 Job description matching
 AI-generated resume rewriting
 Resume PDF export
 Authentication and user dashboard
 Resume history tracking
 AI mock interview system
 Cloud database integration


Security

API keys are stored in .env and never committed to version control
.gitignore is configured to exclude secrets
Compliant with GitHub secret scanning


Contributing
Contributions are welcome. Please open an issue first to discuss what you'd like to change, then submit a pull request.

Author
Developed by Shraddha Upadhye
If you find this project useful, consider giving it a star on GitHub.
