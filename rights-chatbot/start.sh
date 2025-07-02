#!/bin/bash
echo "Starting the rights chatbot using your local LLM..."
uvicorn app:app --reload --host 0.0.0.0 --port 8000
