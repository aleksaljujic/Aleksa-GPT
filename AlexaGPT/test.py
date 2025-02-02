from fastapi import FastAPI
from pydantic import BaseModel
import openai
import uvicorn

app = FastAPI()
openai.api_key = "your_api_key_here"

class RequestBody(BaseModel):
    messages: list

@app.post("/generate")
async def generate_text(body: RequestBody):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=body.messages
    )
    return {"response": response.choices[0].message.content}
