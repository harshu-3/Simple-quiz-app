from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
conn = sqlite3.connect('quiz.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS questions
             (id INTEGER PRIMARY KEY AUTOINCREMENT, question_text TEXT, option1 TEXT, option2 TEXT, option3 TEXT, option4 TEXT, correct_option INTEGER)''')

# Insert sample questions into the database
c.execute("INSERT INTO questions (question_text, option1, option2, option3, option4, correct_option) VALUES (?, ?, ?, ?, ?, ?)",
          ("What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3))

c.execute("INSERT INTO questions (question_text, option1, option2, option3, option4, correct_option) VALUES (?, ?, ?, ?, ?, ?)",
          ("Which programming language is this quiz written in?", "Java", "Python", "C++", "JavaScript", 2))

c.execute("INSERT INTO questions (question_text, option1, option2, option3, option4, correct_option) VALUES (?, ?, ?, ?, ?, ?)",
          ("What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2))

conn.commit()
conn.close()


@app.route('/')
def index():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute("SELECT * FROM questions")
    questions = c.fetchall()
    conn.close()
    return render_template('index.html', questions=questions)


@app.route('/quiz', methods=['POST'])
def quiz():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute("SELECT * FROM questions")
    questions = c.fetchall()
    conn.close()
    return render_template('quiz.html', questions=questions)


@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()

    for key, value in request.form.items():
        if key.startswith("question"):
            question_id = int(key.split("_")[1])
            c.execute("SELECT correct_option FROM questions WHERE id=?", (question_id,))
            correct_option = c.fetchone()[0]
            if int(value) == correct_option:
                score += 1

    conn.close()
    return render_template('result.html', score=score)


if __name__ == '__main__':
    app.run(debug=True)
