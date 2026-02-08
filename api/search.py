from fastapi import APIRouter, UploadFile, File
from services.pdf_service import extract_text_with_ocr

router = APIRouter()

@router.post("/")   # ✅ POST, not GET
async def search_document(keyword: str, file: UploadFile = File(...)):
    """
    Search a keyword in a PDF and return page numbers.
    """

    # Read PDF file
    contents = await file.read()

    # Extract text (digital + OCR)
    text_data = extract_text_with_ocr(contents)

    # Split text into pages
    pages = text_data["full_text"].split("\f")

    # Find keyword (case-insensitive)
    matched_pages = [
        i + 1
        for i, page in enumerate(pages)
        if keyword.lower() in page.lower()
    ]

    return {
        "filename": file.filename,
        "keyword": keyword,
        "pages": matched_pages
    }
