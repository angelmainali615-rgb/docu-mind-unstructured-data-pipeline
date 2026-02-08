import re

def clean_text(text: str) -> str:
    """
    Clean extracted text for NLP processing.
    """
    text = re.sub(r'\r|\n', ' ', text)         # Replace line breaks with space
    text = re.sub(r'\t', ' ', text)            # Remove tabs
    text = re.sub(r'[^A-Za-z0-9.,@\- ]+', '', text)  # Remove special characters
    text = re.sub(' +', ' ', text)             # Normalize multiple spaces
    return text.strip()                         # Remove leading/trailing whitespace
