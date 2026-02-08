from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from services.pdf_service import extract_text_with_ocr
from services.text_cleaner import clean_text
from db.database import save_document
from datetime import datetime

# Define router for upload endpoints
router = APIRouter()

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB limit

@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Accepts a PDF file, validates it, and returns confirmation.
    """
    # Validate file extension
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    # Read file bytes from memory
    contents = await file.read()

    # Validate file size
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File size exceeds 5MB.")

    # Return JSON response
    return JSONResponse(content={"filename": file.filename, "message": "File accepted."})

@router.post("/pdf-text")
async def upload_pdf_text(file: UploadFile = File(...)):
    """
    Accepts a PDF and returns text extracted from it (digital or OCR).
    """
    # Read PDF bytes
    contents = await file.read()

    # Extract text using OCR fallback
    result = extract_text_with_ocr(contents)

    # Return filename, page count, and full text
    return {"filename": file.filename, **result}

@router.post("/pdf-async")
async def upload_pdf_async(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    """
    Accepts PDF, returns immediately, and processes text in the background.
    """
    # Read PDF bytes
    contents = await file.read()

    # Define background task for extraction and cleaning
    def process_file(contents, filename):
        # Extract text
        text_data = extract_text_with_ocr(contents)
        # Clean text
        cleaned = clean_text(text_data["full_text"])
        # Save to database
        save_document(filename, cleaned)

    # Add background task
    background_tasks.add_task(process_file, contents, file.filename)

    # Return task id immediately
    return {"message": "Processing started", "task_id": f"{file.filename}-{datetime.now().timestamp()}"}
