from pdf2image import convert_from_bytes
import pytesseract

# Absolute path to Poppler bin folder
POPPLER_PATH = r"C:\Program Files\poppler-25.07.0\Library\bin"

# Optional: Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_with_ocr(pdf_bytes):
    # Convert PDF to images using the absolute Poppler path
    images = convert_from_bytes(pdf_bytes, poppler_path=POPPLER_PATH)
    text = ""
    
    for img in images:
        text += pytesseract.image_to_string(img)
    
    return text
