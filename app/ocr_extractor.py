# Import function to convert PDF pages into images

from pdf2image import convert_from_bytes
# Import Tesseract OCR engine to read text from images

import pytesseract
import os

POPPLER_PATH = os.path.join(os.getcwd(), "poppler", "Library", "bin")

def extract_text_with_ocr(pdf_bytes):
    text=""
    
    # Convert PDF pages to images
    images = convert_from_bytes(pdf_bytes,poppler_path=POPPLER_PATH)
    print(len(images))
    # OCR each image
    for image in images:
         # Use Tesseract OCR to convert the image into text
        text += pytesseract.image_to_string(image)

    return text