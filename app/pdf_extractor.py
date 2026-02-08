from pypdf import PdfReader
from io import BytesIO

def extract_text_from_pdf(pdf_bytes):
    """
    Extract text from digital PDFs.
    Returns the full text and page count.
    """
    reader = PdfReader(BytesIO(pdf_bytes))
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() or ""
    return full_text, len(reader.pages)
