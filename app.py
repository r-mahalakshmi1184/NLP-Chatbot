from flask import Flask, render_template, request, jsonify
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def get_bot_response(user_input):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM training_data")
    data = cursor.fetchall()
    conn.close()

    questions = [row[0] for row in data]
    answers = [row[1] for row in data]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(questions + [user_input])

    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    best_match = similarity.argmax()

    if similarity[0][best_match] >= 0.4:
     return answers[best_match]
    else:
     return "Data is unavailable."


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = get_bot_response(user_message.lower())
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
