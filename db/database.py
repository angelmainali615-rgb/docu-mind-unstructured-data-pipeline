import sqlite3
from datetime import datetime

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("documents.db", check_same_thread=False)
c = conn.cursor()

# Create table if not exists
c.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY,
    filename TEXT,
    upload_date TEXT,
    clean_text TEXT,
    word_count INTEGER,
    category TEXT
)
""")
conn.commit()

def save_document(filename: str, clean_text: str, category: str = "unknown"):
    """
    Save processed document info to SQLite database.
    """
    word_count = len(clean_text.split())  # Count words
    upload_date = datetime.now().isoformat()  # Current timestamp
    c.execute(
        "INSERT INTO documents (filename, upload_date, clean_text, word_count, category) VALUES (?, ?, ?, ?, ?)",
        (filename, upload_date, clean_text, word_count, category)
    )
    conn.commit()  # Commit changes
