from datetime import datetime, date

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# todo.dbという名前のデータベースを設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# appの情報を基にデータベース読み込み、変数dbに代入
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


# トップページで行う処理
# GET：データベースからすべての投稿を取り出し、それをトップページに渡す
# POST：データベースに投稿を保存
@app.route('/', methods=['GET', 'POST'])    # トップページ(localhost:5000)
def index():
    if request.method == 'GET':
        # Post.due(期限)でソートして全て取得し、内容をpostsに代入する
        posts = Post.query.order_by(Post.due).all()
        return render_template('index.html', posts=posts, today=date.today())

    else:
        # POSTされた内容を受けとる
        title = request.form.get('title')
        detail = request.form.get('detail')
        due = request.form.get('due')
        due = datetime.strptime(due, '%Y-%m-%d')

        # Postクラスに受け取った内容を渡す
        new_post = Post(title=title, detail=detail, due=due)

        # データベースに投稿を保存する
        db.session.add(new_post)
        db.session.commit()

        # トップページにリダイレクト
        return redirect('/')


# 投稿を作成するページを開く処理(保存は"投稿作成"ボタンが押されてトップページに飛んだとき)
@app.route('/create')   # localhost:5000/create
def create():
    return render_template('create.html')


# 詳細ページを表示する処理(idを用いる)
# "詳細"ボタンが押されたときに呼び出される
@app.route('/detail/<int:id>')  # localhost:5000/detail
def detail(id):
    post = Post.query.get(id)
    return render_template('detail.html', post=post)


# todoリストを削除する処理(idを用いる)
# "削除"ボタンが押されたときに呼び出される
@app.route('/delete/<int:id>')  # localhost:5000/delete
def delete(id):
    post = Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/')


# 投稿を変更する処理(idを用いる)
# "変更"ボタンが押されたときに呼び出される
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    post = Post.query.get(id)
    if request.method == 'GET':
        # 1. GET：updateのページに移動("変更"ボタンが押されて'/update/<int:id>'にアクセス時)
        return render_template('update.html', post=post)
    else:
        # 2. POST：updateのページで行った変更をsession.commit()でdbに反映
        post.title = request.form.get('title')
        post.detail = request.form.get('detail')
        post.due = datetime.strptime(request.form.get('due'), '%Y-%m-%d')

        db.session.commit()
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
