import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function Home() {
  const navigate = useNavigate();

  const [resume, setResume] = useState(null);
  const [resumeText, setResumeText] = useState("");
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);

  const analyzeResume = async (e) => {
    e.preventDefault();

    if (!resume && resumeText.trim() === "") {
      alert("Please upload a PDF/DOCX resume or paste resume text.");
      return;
    }

    if (jobDescription.trim() === "") {
      alert("Please enter the Job Description.");
      return;
    }

    const formData = new FormData();

    if (resume) {
      formData.append("resume", resume);
    }

    formData.append("resume_text", resumeText);
    formData.append("job_description", jobDescription);

    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:5000/analyze",
        formData
      );

      navigate("/result", {
        state: {
          result: response.data.result,
        },
      });
    } catch (error) {
      if (error.response) {
        alert(error.response.data.error);
      } else {
        alert("Unable to connect to the backend.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>AI Resume Screening Assistant</h1>

      <form onSubmit={analyzeResume}>

        <label>Upload Resume (PDF / DOCX)</label>

        <input
          type="file"
          accept=".pdf,.docx"
          onChange={(e) => setResume(e.target.files[0])}
        />

        <label>OR Paste Resume</label>

        <textarea
          rows="8"
          placeholder="Paste Resume Here..."
          value={resumeText}
          onChange={(e) => setResumeText(e.target.value)}
        />

        <label>Job Description</label>

        <textarea
          rows="10"
          placeholder="Paste Job Description Here..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        />

        <button type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

      </form>
    </div>
  );
}

export default Home;