// Base URL for the backend. In dev, Vite proxies "/api" to the FastAPI
// server (see vite.config.js). Override with VITE_API_BASE if needed.
const API_BASE = import.meta.env.VITE_API_BASE ?? "/api";

export async function askQuestion(question) {
  const res = await fetch(`${API_BASE}/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  });

  if (!res.ok) {
    const detail = await res.text().catch(() => "");
    throw new Error(`Request failed (${res.status}): ${detail || res.statusText}`);
  }

  return res.json();
}
