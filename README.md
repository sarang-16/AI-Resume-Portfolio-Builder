# 🧠 AI Resume Builder

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=28&duration=3000&pause=1000&color=36BCF7&center=true&vCenter=true&width=900&lines=AI+Resume+Builder;Powered+by+Google+Gemini+AI;Create+Professional+Resumes+in+Seconds;Built+with+Python+and+Streamlit" alt="Typing SVG">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Google-Gemini_AI-green?style=for-the-badge&logo=google">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

---

## 📸 Application Preview

<p align="center">
  <img src="Screenshot%202026-05-02%20003638.png" alt="AI Resume Builder Screenshot" width="1000">
</p>

---

## 🚀 Overview

AI Resume Builder is an intelligent web application that helps users create professional resumes instantly using **Google Gemini AI**.

The application takes user information such as education, skills, projects, certifications, and achievements, then transforms it into a polished and industry-ready resume.

---

## ✨ Features

* 🤖 AI-Powered Resume Generation
* 📝 Professional Resume Content Enhancement
* 🎨 Multiple Resume Templates
* ⚡ Instant Resume Creation
* 👀 Live Resume Preview
* 📥 Download Resume as HTML
* 📋 Structured Resume Sections
* 🌐 Streamlit Web Interface
* 🔥 Gemini AI Integration

---

## 🛠️ Tech Stack

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| Python           | Backend Development       |
| Streamlit        | Web Interface             |
| Google Gemini AI | Resume Content Generation |
| JSON             | Data Formatting           |
| HTML & CSS       | Resume Design             |

---

## 📂 Project Structure

```text
AI-Resume-Builder/
│
├── app.py
├── README.md
├── requirements.txt
├── Screenshot 2026-05-02 003638.png
│
└── Generated Resumes
```

---

## ⚙️ Working Process

```mermaid
graph TD
A[User Enters Information] --> B[Streamlit Form]
B --> C[Google Gemini AI]
C --> D[Resume Content Generation]
D --> E[JSON Processing]
E --> F[HTML Resume Creation]
F --> G[Resume Preview]
G --> H[Download Resume]
```

---

## 📋 Supported Resume Sections

### Personal Information

* Full Name
* Contact Details

### Education

* Degree
* College/University
* Academic Details

### Skills

* Technical Skills
* Soft Skills

### Projects

* Academic Projects
* Personal Projects

### Certifications

* Online Certifications
* Internship Certifications

### Awards

* Achievements
* Recognition

### Languages

* Spoken Languages

---

## 🎨 Available Resume Themes

| Theme          | Color  |
| -------------- | ------ |
| Classic Blue   | Blue   |
| Strange Orange | Orange |
| Funky Yellow   | Yellow |
| Corporate Grey | Grey   |

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI-Resume-Builder.git
cd AI-Resume-Builder
```

### Install Required Packages

```bash
pip install streamlit
pip install google-generativeai
```

Or

```bash
pip install -r requirements.txt
```

### Add Gemini API Key

Replace:

```python
genai.configure(api_key="ENTER YOUR_API_KEY")
```

with your actual Gemini API Key.

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 🎯 Learning Outcomes

This project helped in learning:

* Generative AI Applications
* Prompt Engineering
* Streamlit Development
* API Integration
* JSON Handling
* HTML Resume Design
* User Interface Design
* Python Project Development

---

## 🔮 Future Improvements

* ATS Resume Scoring
* PDF Download Support
* Cover Letter Generator
* Portfolio Website Generator
* Resume Template Gallery
* LinkedIn Integration
* Dark Mode Support

---

## 👨‍💻 Developer

### Sarang Jaiswal

BCA (AI & Data Analytics)

LNCT University

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It motivates future development and improvements.

---

<p align="center">
  Made with ❤️ using Python, Streamlit and Google Gemini AI
</p>
