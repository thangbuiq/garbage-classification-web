from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
import shutil

app = FastAPI()

# Define the upload directory
UPLOAD_DIR = Path("upload")


@app.get("/download/{id}")
async def get_image(id: str):
    try:
        return FileResponse(path=str(UPLOAD_DIR / id))
    except FileNotFoundError:
        return {"error": "Image not found"}


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Save the uploaded file
        upload_path = UPLOAD_DIR / file.filename
        with upload_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {"path": f"Upload successful: {upload_path}"}
    except Exception as e:
        return {"error": f"Server error: {str(e)}"}
