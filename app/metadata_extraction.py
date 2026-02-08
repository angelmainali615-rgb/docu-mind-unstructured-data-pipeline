import re

def extract_metadata(text):
    """
    Extract emails, phone numbers, dates, and numbers.
    """
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    phones = re.findall(r"\d{3}-\d{3}-\d{4}", text)
    date_patterns = [
        r"\d{4}-\d{2}-\d{2}",   # YYYY-MM-DD
        r"\d{2}/\d{2}/\d{4}",   # MM/DD/YYYY
        r"\d{2}-\d{2}-\d{4}",   # DD-MM-YYYY
    ]
    dates = []
    for pattern in date_patterns:
        dates.extend(re.findall(pattern, text))
    numbers = re.findall(r"\b\d[\d,.-]*\b", text)
    return {
        "email": emails[0] if emails else None,
        "phone": phones[0] if phones else None,
        "dates": dates,
        "numbers": numbers
    }
