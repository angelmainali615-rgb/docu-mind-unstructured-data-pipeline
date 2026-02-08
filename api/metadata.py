from fastapi import APIRouter, UploadFile, File
from services.pdf_service import extract_text_with_ocr
from pydantic import BaseModel
import re

# Create router instance
router = APIRouter()

# ✅ REGEX CONSTANTS (OUTSIDE Pydantic models)
EMAIL_REGEX = re.compile(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
)

PHONE_REGEX = re.compile(
    r"\+?\d[\d \-]{7,}\d"
)

DATE_REGEX = re.compile(
    r"\d{2,4}[-/]\d{1,2}[-/]\d{1,2}"
)

# ✅ Pydantic response model (FIELDS ONLY)
class MetadataResponse(BaseModel):
    email: str | None = None
    phone: str | None = None
    dates: list[str] = []

@router.post("/extract", response_model=MetadataResponse)
async def extract_metadata(file: UploadFile = File(...)):
    """
    Extract metadata (email, phone, dates) from a PDF document.
    """

    # Read uploaded PDF into memory
    contents = await file.read()

    # Extract text (digital or OCR)
    text_data = extract_text_with_ocr(contents)

    text = text_data["full_text"]

    # Apply regex extraction
    emails = EMAIL_REGEX.findall(text)
    phones = PHONE_REGEX.findall(text)
    dates = DATE_REGEX.findall(text)

    # Return structured response
    return MetadataResponse(
        email=emails[0] if emails else None,
        phone=phones[0] if phones else None,
        dates=dates
    )
