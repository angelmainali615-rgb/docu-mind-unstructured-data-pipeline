import fitz  # PyMuPDF
from pdf2image import convert_from_bytes
import pytesseract


def extract_text_from_pdf(file_bytes: bytes):
    """
    Extract text from digital PDFs using PyMuPDF.
    """
    pdf_doc = fitz.open(stream=file_bytes, filetype="pdf")  # Open PDF from memory
    full_text = ""  # Initialize text variable
    for page in pdf_doc:  # Iterate pages
        full_text += page.get_text()  # Append page text
    return {
        "page_count": len(pdf_doc),
        "full_text": full_text
    }

def extract_text_with_ocr(file_bytes: bytes):
    """
    Extract text from PDFs, fallback to OCR for scanned pages.
    """
    # Try normal PDF text extraction
    result = extract_text_from_pdf(file_bytes)
    if len(result["full_text"].strip()) > 0:  # If text exists
        return result

    # If no text, perform OCR
    images = convert_from_bytes(file_bytes)  # Convert PDF pages to images
    ocr_text = ""
    for img in images:
        ocr_text += pytesseract.image_to_string(img)  # OCR each image
    return {
        "page_count": len(images),
        "full_text": ocr_text
    }
