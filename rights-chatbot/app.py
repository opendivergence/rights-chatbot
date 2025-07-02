from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>Workplace Disability Advocacy Assistant (Local)</h1><p>Use /chat endpoint to start a conversation.</p>"
