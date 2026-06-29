// Renders the agent's answer plus a compact verification badge.
export default function AnswerCard({ answer, validation }) {
  const status = validation?.status ?? "Unknown";
  const isVerified = status.toLowerCase() === "verified";

  return (
    <div className="answer-card">
      <div className="answer-header">
        <h3 className="section-title">Answer</h3>
        <span className={`status-badge ${isVerified ? "ok" : "warn"}`}>
          {isVerified ? "✓" : "!"} {status}
        </span>
      </div>

      <p className="answer-text">{answer}</p>
    </div>
  );
}
