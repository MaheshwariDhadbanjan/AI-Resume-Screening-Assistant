import os
from google import genai
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from flask import Flask, render_template, request

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():

    resume = request.files['resume']
    job_description = request.form['job_description']

    pdf_reader = PdfReader(resume)

    resume_text = ""

    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    prompt = f"""
Compare the following Resume and Job Description.

Resume:
{resume_text}

Job Description:
{job_description}

Analyze the resume against the job description and return the result in HTML using the following format.

<b>Resume Match Score:</b> Percentage

<b>Candidate Strengths:</b>
- Point 1
- Point 2

<b>Missing Skills:</b>
- Point 1
- Point 2

<b>Recommended Interview Questions:</b>
1. Question
2. Question
3. Question
4. Question
5. Question

<b>Overall Hiring Recommendation:</b>
One short sentence.

<b>Role Recommendations:</b>
- Role 1
- Role 2

<b>Training Recommendations:</b>
- Training 1
- Training 2

Rules:
- Keep the response short.
- Base the analysis only on the uploaded resume and job description.
- Do not use markdown symbols like ** or ##.
- Return only HTML.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>AI Resume Analysis</title>
</head>

<body>

<h2>AI Resume Analysis</h2>

{response.text}

<br><br>

<a href="/">Analyze Another Resume</a>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(debug=True)