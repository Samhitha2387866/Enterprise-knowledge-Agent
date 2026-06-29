#!/usr/bin/env bash
# Start the FastAPI backend using the project venv (no activation needed).
cd "$(dirname "$0")"
exec ./venv/bin/uvicorn main:app --reload "$@"
