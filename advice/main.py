import openai
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("API_KEY")

class trash(BaseModel):
    type_trash:  str

def input_trash(input):
    messages = [
    {"role": "system", "content":"Act as an environmental advocate, your task offers a brief simple and friendly tip on handling garbage."}
    ]
    messages.append(
        {"role": "user", "content": f"{input}"},
)
    chat = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo', messages=messages
    )
    reply = chat.choices[0].message.content
    return reply
#Initialize FastAPI
app = FastAPI()

@app.get("/")
async def ok_endpoint():
    return {"message": "ok"}


@app.post("/get-advice")
async def give_advice(Trash: trash ):
    advice = input_trash(f"Garbage name: {Trash.type_trash}")
    return {"Advice": advice}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
