import re 

def clean_text(text):
    #Remove special characters
     text=re.sub(r"[^a-zA-Z0-9\s\-\.]+"," ",text)
     
     # Remove broken line breaks
      # \n+ → one or more consecutive line breaks
     text = re.sub(r"\n+", " ", text)
     
     # Normalize spaces
     text = re.sub(r"\s+", " ", text)
     
    # Replace different types of dashes (–, —, ‑) with normal ASCII dash
     text = text.replace('–', '-').replace('—', '-').replace('‑', '-')

     return text.strip()

     
     