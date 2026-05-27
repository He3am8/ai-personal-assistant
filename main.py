from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI bot is running"}

@app.get("/chat")
def chat(msg: str):
    return {
        "input": msg,
        "reply": "version 1 - no AI yet"
    }
