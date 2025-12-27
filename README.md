# NLP-Chatbot
AI-powered FAQ chatbot using natural language queries. Retrieves the most relevant answer from a training dataset stored in SQLite using TF-IDF and cosine similarity.
An AI-powered FAQ chatbot that responds to user queries using natural language. The system stores training data in an SQLite database and finds the most relevant answer using **TF-IDF** and **cosine similarity**. If no suitable answer is found, it gracefully responds with "Data is unavailable."

## Features
- Natural language query support
- SQLite database for training data storage
- TF-IDF vectorization for question similarity
- Cosine similarity-based answer retrieval
- Simple Flask web interface
- JSON API support for chatbot interaction

## Requirements
- Python 3.8+
- Flask
- scikit-learn
- sqlite3 (built-in)
- CSV file for training data

Install required packages:

```bash
pip install Flask scikit-learn
