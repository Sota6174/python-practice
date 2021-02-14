# 実行コマンド >py test.py

from flask import Flask

app = Flask(__name__)


@app.route('/')     # トップページ
def index():
    return '<h1>Hello World<h1><p>TodoApp</p>'


if __name__ == "__main__":
    app.run(debug=True)
