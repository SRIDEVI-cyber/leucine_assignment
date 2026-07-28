from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.utils import extract_pdf_text
from app.rag import add_documents

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    filepath = f"uploads/{file.filename}"

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_pdf_text(filepath)

    add_documents(text)

    return {
        "message": "PDF uploaded successfully",
        "filename": file.filename
    }