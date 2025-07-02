from fastapi import FastAPI, Request
from pydantic import BaseModel
import subprocess
import json

app = FastAPI()

# Define input model
class ChatRequest(BaseModel):
    role: str  # "employee" or "manager"
    state: str  # e.g., "WA"
    question: str

@app.get("/")
def home():
    return {"message": "Workplace Disability Advocacy Assistant (Local)"}

@app.post("/chat")
def chat(req: ChatRequest):
    prompt = build_prompt(req.role, req.state, req.question)
    response = run_ollama(prompt)
    return {"response": response.strip()}

# --- Helpers below ---

def build_prompt(role, state, question):
    return f"""
You are a legal and workplace accessibility assistant for neurodivergent and disabled employees. 
Respond as if you are a local-first assistant, prioritizing psychological safety and plain language. 
This user is a {role} in the state of {state} and is asking:

"{question}"

Use ADA, EEOC, FMLA, and state law if relevant. Respond with clarity, without legal jargon.
"""

def run_ollama(prompt):
    # Run your local LLM via Ollama (default: phi3 or mistral)
    process = subprocess.run(
        ["ollama", "run", "phi3", prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return process.stdout or "Error: No response from model."
