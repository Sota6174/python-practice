from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# todo.dbという名前のデータベースを設定
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///todo.db'
# データベースを作成
db = SQLAlchemy(app)


class Post(db.Model):
    # id: 整数値, 主キーに設定
    id = db.Column(db.Integer, primary_key=True)
    # title: 30字以内の文字列, 空はNGで設定
    title = db.Column(db.String(30), nullable=False)
    # detail: 100字以内の文字列, 空でもOKで設定
    detail = db.Column(db.String(100))
    # due: 日付型, 空はNGで設定
    due = db.Column(db.DateTime, nullable=False)


# トップページでCreateボタンを押すことで送られるPOSTメソッドを受け入れる
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/create')
def create():
    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)
