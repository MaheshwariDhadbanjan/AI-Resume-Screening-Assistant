import os
from google import genai
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from docx import Document
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

    resume = request.files.get('resume')
    resume_text_input = request.form.get('resume_text', '').strip()
    job_description = request.form.get('job_description', '').strip()

    resume_text = ""

    # -------------------------------
    # Read uploaded file if available
    # -------------------------------
    if resume and resume.filename != "":

        filename = resume.filename.lower()

        try:
            if filename.endswith(".pdf"):

                pdf_reader = PdfReader(resume)

                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text:
                        resume_text += text

            elif filename.endswith(".docx"):

                document = Document(resume)

                for para in document.paragraphs:
                    resume_text += para.text + "\n"

            else:
                return """
                <h3>Invalid file format.</h3>
                <p>Please upload only PDF or DOCX files.</p>
                <a href="/">Go Back</a>
                """

        except Exception as e:
            return f"""
            <h3>Error reading uploaded file.</h3>
            <p>{e}</p>
            <a href="/">Go Back</a>
            """

    # -------------------------------
    # Use pasted resume text
    # -------------------------------
    elif resume_text_input:
        resume_text = resume_text_input

    else:
        return """
        <h3>No Resume Provided</h3>
        <p>Please upload a PDF/DOCX resume or paste resume text.</p>
        <a href="/">Go Back</a>
        """

    prompt = f"""
Compare the following Resume and Job Description.

Resume:
{resume_text}

Job Description:
{job_description}

Analyze the resume against the job description and return the result in HTML using the following format.

<b>Resume Match Score:</b> Percentage

<h4>Candidate Strengths:</h4>
<ul>
<li>Point 1</li>
<li>Point 2</li>
</ul>

<b>Missing Skills:</b>
<ul>
<li>Point 1</li>
<li>Point 2</li>
</ul>

<b>Recommended Interview Questions:</b>
<ol>
<li>Question</li>
<li>Question</li>
<li>Question</li>
<li>Question</li>
<li>Question</li>
</ol>

<b>Overall Hiring Recommendation:</b>
<p>One short sentence.</p>

<b>Role Recommendations:</b>
<ul>
<li>Role 1</li>
<li>Role 2</li>
</ul>

<b>Training Recommendations:</b>
<ul>
<li>Training 1</li>
<li>Training 2</li>
</ul>

Rules:

Return only HTML.

Keep the response concise.

Base the analysis only on the uploaded resume and job description.

Do not use Markdown symbols like ** or ##.
"""

    try:

        response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

        return render_template(
            "result.html",
            result=response.text
        )

    except Exception as e:

        return f"""
        <h2>Something went wrong.</h2>
        <p>{e}</p>
        <a href="/">Try Again</a>
        """


if __name__ == "__main__":
    app.run(debug=True)