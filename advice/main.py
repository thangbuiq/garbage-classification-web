import openai
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

openai.api_key = "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"
class trash(BaseModel):
    type_trash:  str

def input_trash(input):
    messages = [
    {"role": "system", "content":"Provide a brief piece of advice on handling garbage"}
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
    return {"product_description": advice}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)