from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import FileResponse
from pathlib import Path
import uvicorn
import shutil
import os


app = FastAPI()

# Define the upload directory
UPLOAD_DIR = Path("upload")


@app.get("/download/{id}")

async def get_image(request: Request, id: str):
    try:
        current_ip = request.client.host
        return {"path": f"http://{current_ip}:8000/{UPLOAD_DIR}/{id}"}
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