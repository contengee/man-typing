from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Herokuにデプロイされた場合は、Herokuが提供する環境変数からデータベースの接続情報を取得します
if 'DATABASE_URL' in os.environ:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
else:
    # Heroku以外の環境
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

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
    return render_template('index.html')  # index.htmlはフロントエンドのHTMLファイル名です。

@app.route('/api/word')
def random_word():
    word = random.choice(Word.query.all())
    return jsonify(word=word.word)

if __name__ == "__main__":
    db.create_all()  # データベースとテーブルを作成します。
    app.run(debug=True)
