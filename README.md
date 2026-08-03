# 🤖 AI Resume Screening System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![NLP](https://img.shields.io/badge/NLP-spaCy-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

</p>

---

# 📌 Project Overview

The **AI Resume Screening System** is an AI-powered recruitment application that automates resume screening using **Natural Language Processing (NLP)** and **Machine Learning**.

Instead of manually reviewing hundreds of resumes, recruiters can upload resumes and a job description. The system extracts candidate information, compares resumes with the job description, calculates a matching score, ranks candidates, and recommends the most suitable applicants.

---

# 🚀 Project Highlights

- 🤖 AI-Powered Resume Screening
- 📄 Resume Parsing (PDF & DOCX)
- 🧠 NLP-based Skill Extraction
- 📊 Resume Matching Score
- 🏆 Candidate Ranking
- 💼 Job Description Matching
- 📈 Interactive Dashboard
- 📥 Download Screening Report
- 🔐 Login & Registration
- 🗄 SQLite Database
- 📂 Resume Upload
- 📋 Recruiter-Friendly Interface

---

# 📷 Screenshots

## 🔐 Login Page

> Add image here

```
screenshots/login.png
```

---

## 📊 Dashboard

> Add image here

```
screenshots/dashboard.png
```

---

## 📄 Resume Analysis

> Add image here

```
screenshots/result.png
```

---

# ✨ Features

### Resume Management

- Upload PDF Resume
- Upload DOCX Resume
- Multiple Resume Support
- Resume Parsing

### AI Analysis

- Skill Extraction
- Experience Detection
- Education Detection
- Certification Detection
- Project Detection
- Keyword Matching
- Resume Similarity
- ATS Score

### Candidate Evaluation

- Resume Score
- Missing Skills
- Matching Percentage
- Candidate Ranking
- Shortlisting

### Reports

- Download Report
- Resume Summary
- Skill Analysis

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | Web Interface |
| Scikit-learn | Machine Learning |
| spaCy | NLP |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| SQLite | Database |
| PDFPlumber | PDF Reader |
| python-docx | DOCX Reader |
| Matplotlib | Visualization |
| Git | Version Control |
| GitHub | Repository Hosting |

---

# 📚 Python Libraries

```python
streamlit
pandas
numpy
scikit-learn
spacy
sqlite3
pdfplumber
python-docx
matplotlib
re
os
```

---

# 📂 Project Structure

```
AI-Resume-Screening-System/

│
├── app.py
├── login.py
├── database.py
├── resume_parser.py
├── skill_extractor.py
├── matcher.py
├── ranking.py
├── report_generator.py
├── utils.py
├── requirements.txt
│
├── database/
│      resumes.db
│
├── assets/
│      style.css
│
├── screenshots/
│      login.png
│      dashboard.png
│      result.png
│
├── sample_data/
│      resume1.pdf
│      resume2.pdf
│      job_description.txt
│
└── README.md
```

---

# ⚙ System Architecture

```
Recruiter
      │
      ▼
Upload Resume
      │
      ▼
Resume Parser
      │
      ▼
Text Extraction
      │
      ▼
Skill Extraction (NLP)
      │
      ▼
Job Description Matching
      │
      ▼
Resume Score Calculation
      │
      ▼
Candidate Ranking
      │
      ▼
Dashboard & Report
```

---

# 🔄 Workflow

```
Login
   │
   ▼
Upload Resume
   │
   ▼
Extract Resume Text
   │
   ▼
Extract Skills
   │
   ▼
Compare with Job Description
   │
   ▼
Calculate ATS Score
   │
   ▼
Rank Candidate
   │
   ▼
Generate Report
```

---

# 📊 Candidate Evaluation Criteria

The AI evaluates resumes based on:

- Skills Match
- Experience
- Education
- Projects
- Certifications
- Technical Keywords
- Resume Similarity
- ATS Compatibility

---

# 📈 Output

The application generates:

- Resume Score
- ATS Score
- Skill Match Percentage
- Missing Skills
- Candidate Ranking
- Recommendation
- Downloadable Report

---

# 💼 Applications

- HR Recruitment
- Campus Placement
- Internship Selection
- Corporate Hiring
- Recruitment Agencies
- Job Portals

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Screening-System.git
```

### Move into Project

```bash
cd AI-Resume-Screening-System
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

# 📦 Requirements

```
Python 3.10+
Streamlit
spaCy
Scikit-learn
Pandas
NumPy
SQLite
PDFPlumber
python-docx
Matplotlib
```

---

# 🌟 Future Enhancements

- Resume Recommendation System
- AI Interview Question Generator
- Resume ATS Improvement Suggestions
- Multi-language Resume Support
- Email Notifications
- Cloud Database
- Recruiter Dashboard
- Resume Analytics
- Candidate Comparison
- Resume Duplicate Detection

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to GitHub
5. Create a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Developer

**Vamshi C**

**B.Tech – Computer Science & Engineering (AI & ML)**

Passionate about AI, Machine Learning, Data Science, and Full Stack Development.

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork this repository

📢 Share it with others

---

## ❤️ Thank You

Thank you for visiting this project. Feedback and suggestions are always welcome!
