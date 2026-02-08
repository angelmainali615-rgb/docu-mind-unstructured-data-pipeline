from fastapi import FastAPI, UploadFile, File, HTTPException
from .pdf_extractor import extract_text_from_pdf
from .ocr_extractor import extract_text_with_ocr
from .text_cleaning import clean_text
from .metadata_extraction import extract_metadata
from .keyword_extraction import extract_keywords

app = FastAPI()

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

@app.post("/upload/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")
    
    pdf_bytes = await file.read()

    # Validate file size
    if len(pdf_bytes) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large")

    # Try digital PDF extraction
    text, page_count = extract_text_from_pdf(pdf_bytes)

    # If digital extraction fails, use OCR
    if len(text.strip()) == 0:
        text = extract_text_with_ocr(pdf_bytes)

    metadata = extract_metadata(text)
    cleaned_text = clean_text(text)
    keywords = extract_keywords(cleaned_text)

    return {
        "filename": file.filename,
        "page_count": page_count,
        "clean_text": cleaned_text,
        "metadata": metadata,
        "keywords": keywords
    }
