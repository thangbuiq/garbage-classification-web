from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
import uvicorn
import shutil
import os

PUBLIC_IP_ADDRESS = os.environ.get("PUBLIC_IP_ADDRESS")
PUBLIC_DNS_ADDRESS = os.environ.get("PUBLIC_DNS_ADDRESS")
origins = [ 
    f"http://{PUBLIC_IP_ADDRESS}:8888",
    f"http://{PUBLIC_IP_ADDRESS}:8000",
    f"http://{PUBLIC_DNS_ADDRESS}:8888",
    f"http://{PUBLIC_DNS_ADDRESS}:8000",
    "http://localhost:8888",
    "http://localhost:8000"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Define the upload directory
UPLOAD_DIR = Path("upload")

@app.get("/download/{id}")
async def get_image(id: str):
    try:
        file_path = UPLOAD_DIR / id
        return FileResponse(file_path)
    except FileNotFoundError:
        return {"error": "Image not found"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        if not os.path.exists(UPLOAD_DIR):
            os.mkdir(UPLOAD_DIR)

        # Save the uploaded file
        upload_path = UPLOAD_DIR / file.filename
        with upload_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {"path": f"Upload successful: {upload_path}"}
    except Exception as e:
        return {"error": f"Server error: {str(e)}"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
