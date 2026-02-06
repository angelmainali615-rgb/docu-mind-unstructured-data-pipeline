from pypdf import PdfReader #reads digital PDFs
from io import BytesIO #lets PDF be read from memory

def extract_text_from_pdf(pdf_bytes):
    #open PDF from memory 
    reader=PdfReader(BytesIO(pdf_bytes))
    
    full_text = ""
    
    #reader.pages : a list of all the pages in your PDF.
    for page in reader.pages: #Go through every page in the PDF, one by one.
        #extract_text() : a method provided by PyPDF.
        full_text += page.extract_text() or ""

    return full_text, len(reader.pages)