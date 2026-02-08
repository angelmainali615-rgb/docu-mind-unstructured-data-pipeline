import spacy
from collections import Counter

# Load small English NLP model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text: str, top_n: int = 10):
    """
    Extract top N keywords from text, ignoring stop words.
    """
    doc = nlp(text.lower())  # Convert text to lowercase
    words = [token.text for token in doc if token.is_alpha and not token.is_stop]  # Filter words
    freq = Counter(words)  # Count word frequencies
    return freq.most_common(top_n)  # Return top N words

