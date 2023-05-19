from app import app, db, Word  # appはあなたのFlaskアプリケーションのファイル名

# 単語をデータベースに追加
words = ["apple", "banana", "cherry", "date", "elderberry"]

with app.app_context():
    db.create_all()  # データベースにテーブルを作成
    for word in words:
        word = Word(word=word)
        db.session.add(word)

    db.session.commit()  # 変更をデータベースに保存
