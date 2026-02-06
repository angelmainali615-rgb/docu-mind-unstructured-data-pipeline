# Import FastAPI to create an API
from fastapi import FastAPI,UploadFile, File,HTTPException
from .pdf_extractor import extract_text_from_pdf
from .ocr_extractor import extract_text_with_ocr
from .text_cleaning import clean_text
from .metadata_extraction import extract_metadata
from .keyword_extraction import extract_keywords

# Create FastAPI app
app=FastAPI()
# Set maximum file size = 5MB
MAX_FILE_SIZE = 5 * 1024 * 1024

@app.post("/upload/pdf")
async def upload_pdf(file: UploadFile=File(...)):
     # Check if file is PDF
     if  not file.filename.endswith(".pdf"):
         raise HTTPException(status_code=400,detail="only PDF files allowed")
     
    
      # Read file into memory (RAM)
     pdf_bytes = await file.read()
     
      # Check file size
     if len(pdf_bytes)>MAX_FILE_SIZE:
         raise HTTPException(status_code=400,detail="File too large")
    # Try digital PDF extraction
     text, page_count = extract_text_from_pdf(pdf_bytes)
     print("PAGE COUNT:", page_count)
     print("RAW TEXT:\n", text)

    # If text is empty : OCR
     if len(text.strip()) == 0:
        text = extract_text_with_ocr(pdf_bytes)
     
     
     metadata = extract_metadata(text)
     
     
     

    # Clean text
     cleaned_text = clean_text(text)
     

     
     Keywords = extract_keywords(cleaned_text)
     

    # Return JSON response
     return {
        "filename": file.filename,
        "page_count": page_count,
        "clean_text": cleaned_text,
        "metadata": metadata,
        "Keywords": Keywords
    }
          
 
