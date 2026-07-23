# AI Resume Screening Assistant

## 📌 Project Description

The AI Resume Screening Assistant is a web application that analyzes a candidate's resume against a given job description using Google Gemini AI. It provides an AI-generated resume match score, strengths, missing skills, interview questions, hiring recommendations, and suggested learning areas to help candidates prepare for job opportunities.

---

## 🚀 Features

- Upload Resume (PDF or DOCX)
- Paste Resume Text
- Enter Job Description
- AI-powered Resume Analysis
- Resume Match Score
- Candidate Strengths
- Missing Skills
- Recommended Interview Questions
- Overall Hiring Recommendation
- Suitable Role Recommendations
- Training Recommendations

---

## 🛠 Technologies Used

### Frontend
- React
- JavaScript
- HTML
- CSS
- Axios
- React Router

### Backend
- Python
- Flask
- Flask-CORS

### AI Integration
- Google Gemini AI

### Python Libraries
- google-genai
- PyPDF2
- python-docx
- python-dotenv

---

## 📂 Project Structure

```
AI-Resume-Screening-Assistant
│
├── frontend
│   ├── App.jsx
│   ├── Home.jsx
│   ├── Result.jsx
│   ├── main.jsx
│   ├── App.css
│   └── package.json
│
├── backend
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
└── README.md
```

---

## 📷 Screenshots

### Home Page

![Home Page](Screenshot/home_page.png)

### Result Page

![Result Page 1](Screenshot/result1_page.png)

![Result Page 2](Screenshot/result2_page.png)

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AI-Resume-Screening-Assistant
```

### 2. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project folder and add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 4. Run the Flask Backend

```bash
python app.py
```

The backend will start at:

```
http://127.0.0.1:5000
```

### 5. Run the React Frontend

```bash
npm install
npm run dev
```

The frontend will start at:

```
http://localhost:5173
```

---

## 🔄 Project Workflow

```
User Uploads Resume
        │
        ▼
React Frontend
        │
        ▼
Axios POST Request
        │
        ▼
Flask Backend
        │
        ▼
Extract Resume Text
        │
        ▼
Google Gemini AI
        │
        ▼
Generate Resume Analysis
        │
        ▼
Return JSON Response
        │
        ▼
React Result Page
```

---

## 📋 Output

The application generates:

- Resume Match Score
- Candidate Strengths
- Missing Skills
- Interview Questions
- Hiring Recommendation
- Role Recommendations
- Training Recommendations

---

## 👩‍💻 Author

**Maheshwari**
