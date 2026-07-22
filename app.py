import os
from google import genai
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from PyPDF2 import PdfReader
from docx import Document

load_dotenv()

app = Flask(__name__)
CORS(app)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_resume_text(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        pdf_reader = PdfReader(file)
        text = ""

        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        return text

    elif filename.endswith(".docx"):
        doc = Document(file)
        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    return ""


@app.route("/")
def home():
    return jsonify({"message": "AI Resume Screening Backend Running"})


@app.route("/analyze", methods=["POST"])
def analyze():

    job_description = request.form.get("job_description")
    resume_text = request.form.get("resume_text", "").strip()

    if "resume" in request.files:
        file = request.files["resume"]

        if file.filename != "":
            resume_text = extract_resume_text(file)

    if not resume_text:
        return jsonify({
            "error": "Please upload a PDF/DOCX resume or enter resume text."
        }), 400

    prompt = f"""
Compare the following Resume and Job Description.

Resume:
{resume_text}

Job Description:
{job_description}

Return ONLY HTML.

Use this format:

<h2>Resume Match Score</h2>
<p>85%</p>

<h2>Candidate Strengths</h2>
<ul>
<li>Strength 1</li>
<li>Strength 2</li>
<li>Strength 3</li>
</ul>

<h2>Missing Skills</h2>
<ul>
<li>Skill 1</li>
<li>Skill 2</li>
<li>Skill 3</li>
</ul>

<h2>Recommended Interview Questions</h2>
<ol>
<li>Question 1</li>
<li>Question 2</li>
<li>Question 3</li>
<li>Question 4</li>
<li>Question 5</li>
</ol>

<h2>Overall Hiring Recommendation</h2>
<p>One short sentence.</p>

<h2>Role Recommendations</h2>
<ul>
<li>Role 1</li>
<li>Role 2</li>
</ul>

<h2>Training Recommendations</h2>
<ul>
<li>Training 1</li>
<li>Training 2</li>
</ul>

Rules:

Return only HTML.

Do not use markdown.

Keep the response short.
"""

    try:

        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return jsonify({
            "result": response.text
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)