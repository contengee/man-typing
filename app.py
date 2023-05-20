from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    DATABASE_URL = 'sqlite:////tmp/test.db'
elif DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return '<Word %r>' % self.word

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/word')
def random_word():
    word = random.choice(Word.query.all())
    return jsonify(word=word.word)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
