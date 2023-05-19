from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

#if os.environ.get('DATABASE_URL') is None: # ローカル
#    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite:////tmp/test.db'
#    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#else:
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
#    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'] # Heroku

SQLALCHEMY_DATABASE_URI = 'postgres:///ddsllujzsltuhx:db525577117eb2c7661c4e13e7bb9894039eff2a80699fec05bc65dd8a706005@ec2-34-193-110-25.compute-1.amazonaws.com:5432/d7696h6kmr48s0'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'] # Heroku
    
db = SQLAlchemy(app)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(80), unique=True, nullable=False)

#    def __init__(self, word):
#        self.word = word

    def __repr__(self):
        return '<Word %r>' % self.word

@app.route('/')
def index():
    return render_template('index.html')  # index.htmlはフロントエンドのHTMLファイル名です。

@app.route('/api/word')
def random_word():
    word = random.choice(Word.query.all())
    return jsonify(word=word.word)

if __name__ == "__main__":
    db.create_all()  # データベースとテーブルを作成します。
    app.run(debug=True)
