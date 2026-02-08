# 📄 Docu-Mind – PDF Parsing & NLP Engine

Docu-Mind is a **FastAPI-based microservice** that ingests PDF documents, extracts text (including OCR for scanned PDFs), cleans and structures the data, and prepares it for **Machine Learning and NLP pipelines**.

This project demonstrates how real-world systems handle **unstructured and messy documents** before modeling.

---

## 🚀 Key Features

- Secure PDF upload with validation
- Digital PDF text extraction (PyMuPDF)
- OCR fallback for scanned PDFs (Tesseract)
- Text cleaning and normalization
- Metadata extraction (email, phone, dates)
- Keyword extraction using NLP
- Keyword-based document search
- SQLite dataset storage
- Async background processing

---

## 🧠 Tech Stack

- **API:** FastAPI  
- **PDF Processing:** PyMuPDF  
- **OCR:** Tesseract + pdf2image  
- **NLP:** spaCy  
- **Database:** SQLite  
- **Language:** Python 3.9+

---

## 📁 Project Structure
ocu_mind/
├── main.py
├── api/
├── services/
├── db/
├── requirements.txt
└── README.md


---

## ⚙️ Setup & Run

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn main:app --reload

