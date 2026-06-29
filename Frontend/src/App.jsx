import { useState } from "react";
import { askQuestion } from "./api.js";
import AnswerCard from "./components/AnswerCard.jsx";

export default function App() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    const trimmed = question.trim();
    if (!trimmed || loading) return;

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const data = await askQuestion(trimmed);
      setResult(data);
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">
      <header className="header">
        <h1>Enterprise Knowledge Agent</h1>
        <p className="subtitle">Ask a question about your enterprise documents.</p>
      </header>

      <form className="ask-form" onSubmit={handleSubmit}>
        <textarea
          className="question-input"
          placeholder="Ask a question…"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) handleSubmit(e);
          }}
          rows={3}
        />
        <div className="form-row">
          <button
            type="submit"
            className="ask-button"
            disabled={loading || !question.trim()}
          >
            {loading ? "Thinking…" : "Ask"}
          </button>
        </div>
      </form>

      {error && <div className="error-box">⚠️ {error}</div>}

      {result && (
        <div className="results">
          <AnswerCard answer={result.answer} validation={result.validation} />
        </div>
      )}
    </div>
  );
}
