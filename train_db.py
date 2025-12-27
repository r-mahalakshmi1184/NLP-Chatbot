import sqlite3
import csv

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS training_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
)
""")

# Read CSV file and insert data
with open("chatbot_data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO training_data (question, answer) VALUES (?, ?)",
            (row["question"].lower(), row["answer"])
        )

conn.commit()
conn.close()

print("Database created and dataset inserted successfully!")
