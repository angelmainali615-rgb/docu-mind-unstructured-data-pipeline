import re

def clean_text(text):
    """
    Clean the extracted text:
    - Remove special characters
    - Fix line breaks and extra spaces
    - Normalize dashes
    """
    # Remove unwanted characters
    text = re.sub(r"[^a-zA-Z0-9\s\-\.]+", " ", text)
    
    # Replace multiple line breaks with a space
    text = re.sub(r"\n+", " ", text)
    
    # Normalize spaces
    text = re.sub(r"\s+", " ", text)
    
    # Normalize different types of dashes to '-'
    text = text.replace("–", "-").replace("—", "-").replace("‑", "-")
    
    return text.strip()
