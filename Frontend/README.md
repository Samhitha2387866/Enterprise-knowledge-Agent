# Enterprise Knowledge Agent — Frontend

A React + Vite UI for the FastAPI backend. It sends questions to the
`/ask` endpoint and displays the agent's answer, the Retrieve → Analyze →
Verify pipeline, and the verification result (status + confidence).

## Setup

```bash
cd Frontend
npm install
npm run dev
```

The app runs at http://localhost:5173.

## Backend

Start the FastAPI backend (default port 8000) from the `Backend` folder:

```bash
cd Backend
uvicorn main:app --reload
```

In dev, Vite proxies `/api/*` → `http://127.0.0.1:8000` (see
[vite.config.js](vite.config.js)), so no CORS setup is required. To point at a
different backend, set `VITE_API_BASE` (e.g. `VITE_API_BASE=http://host:8000`).

## API contract

`POST /ask` with `{ "question": "..." }` returns:

```json
{
  "answer": "string",
  "validation": { "status": "Verified", "reason": "...", "confidence": 90 },
  "agent_flow": ["Retrieve", "Analyze", "Verify"]
}
```
