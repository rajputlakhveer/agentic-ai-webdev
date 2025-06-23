
from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat")
def chat(msg: Message):
    reply = run_agent(msg.message)
    return {"reply": reply}
