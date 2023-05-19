from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# 単語リスト。実際にはもっと大きなリストにするか、
# 外部のデータソース（データベースやAPI）から取得します。
words = ["apple", "banana", "cherry", "date", "elderberry"]

@app.route('/')
def index():
    return render_template('index.html')  # index.htmlはフロントエンドのHTMLファイル名です。

@app.route('/api/word')
def random_word():
    word = random.choice(words)
    return jsonify(word=word)

if __name__ == "__main__":
    app.run(debug=True)
