from collections import Counter

def extract_keywords(text, top_n=10):
    """
    Extract top keywords from text (excluding stopwords)
    """
    stopwords = {"the","is","on","in","at","and","to","of","for","with","by"}
    
    # Split text into words, lowercase and filter stopwords
    words = [w for w in text.lower().split() if w not in stopwords and len(w) > 2]
    
    # Count frequency and return top_n keywords
    return Counter(words).most_common(top_n)
