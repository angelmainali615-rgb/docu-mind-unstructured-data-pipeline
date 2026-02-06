#Counter is a special dictionary for counting how many times each item appears.
from collections import Counter
def extract_keywords(text,top_n=10):
    words=text.lower().split()
    
    stopwords={"the","is","on","in","at","and","to","of","for","with","by"}
    
    filtered_words=[
        word for word in words if word  not in stopwords and len(word)>2
    ]
    word_counts=Counter(filtered_words)
    
    return word_counts.most_common(top_n)