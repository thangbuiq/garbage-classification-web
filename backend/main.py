from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
from utils import predict, zeroshot, input_trash
import time
import datetime
import uvicorn
import shutil
import os
import pytz

origins = [ 
    "https://garbage-classification-web.vercel.app"
]

app = FastAPI(
    title="Garbage Classification",
    summary= "This is an API that helps users classify waste and learn how to handle it"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

class trash(BaseModel):
    type_trash:  str

@app.get("/")
async def live():

    return {
        "message": "Your service is live 🎉",
        "time": datetime.datetime.now(pytz.timezone("Asia/Ho_Chi_Minh")).strftime("%Y-%m-%d %H:%M:%S")
    }

@app.post("/predict-resnet")
async def predict_endpoint(file: UploadFile = File(...)):
    if True:
        return {
            "message": "Our server is weak so this server is deprecated!"
        }

    # Save the uploaded file
    upload_path = f"/tmp/{(datetime.datetime.now()).timestamp()}.png"

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    predicted_value, predicted_accuracy = await predict(upload_path)

    return {
        "path": upload_path,
        "predicted_value": predicted_value,
        "predicted_accuracy": predicted_accuracy
    }

@app.post("/predict")
async def predict_zeroshot(file: UploadFile = File(...)):
    try:
        # Save the uploaded file
        upload_path = f"/tmp/{(datetime.datetime.now()).timestamp()}.png"

        with open(upload_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        predicted_value, predicted_accuracy = await zeroshot(upload_path)

        return {
            "path": upload_path,
            "predicted_value": predicted_value,
            "predicted_accuracy": predicted_accuracy
        }
    except Exception as e:
        return {
            "error": str(e)
        }

@app.post("/get-advice")
async def give_advice(Trash: trash ):
    start_time = time.time()
    advice = input_trash(f"Loại rác: {Trash.type_trash}")
    return {
        "advice": advice,
        "time": time.time() - start_time
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=os.getenv("PORT",8000),
        reload=True
    )
