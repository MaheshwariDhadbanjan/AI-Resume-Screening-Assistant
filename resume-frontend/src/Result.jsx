import { useLocation, useNavigate } from "react-router-dom";

function Result() {
  const location = useLocation();
  const navigate = useNavigate();

  const result = location.state?.result;

  if (!result) {
    return (
      <div className="container">
        <h2>No Analysis Found</h2>
        <p>Please analyze a resume first.</p>

        <button onClick={() => navigate("/")}>
          Go Back
        </button>
      </div>
    );
  }

  return (
    <div className="container">

      <h1>AI Resume Analysis</h1>

      <div
        className="result-box"
        dangerouslySetInnerHTML={{ __html: result }}
      />

      <button
        style={{ marginTop: "20px" }}
        onClick={() => navigate("/")}
      >
        Analyze Another Resume
      </button>

    </div>
  );
}

export default Result;