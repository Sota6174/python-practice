# WebAppPrimer

- pythonとFlaskでWebアプリを作成する
- 表示の見た目を整えるのにBootstrapをダウンロードし使用した

# 仮想環境の構築

- [Issueのリンク](https://github.com/Sota6174/python-practice/issues/6#issue-807942767)

# bootstrapを使用する環境の構築

- 表示の見た目を整えるのにBootstrapをダウンロードし使用した
1. bootstrap-5.0.0-beta1-distフォルダのcssファイルのみをstaticフォルダ内にコピーする

# 実行時

0. dbを作成する(todo.dbが作られればOK)
```
> py
>>> from test4 import db
>>> db.create_all()
>>> quit()
```
1. ターミナルで```py test4.py```などファイルを実行する
2. Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)と言われるので、http://127.0.0.1:5000/ に飛ぶ
3. 開いたページがトップページを表すので、そこから実装通りにページを移動していく(例. http://127.0.0.1:5000/create)

# 参考動画

- [はやたす / Pythonエンジニア](https://www.youtube.com/watch?v=9JDFVEur0Xs&list=PL4Y-mUWLK2t2rISQza73yNiz6_8HTaQiY&index=23)さんの動画

# モジュールのインポート

- repuirements.txtに記載

# メモ

- 実行時の0番でエラーを出された
- 原因は```SQLALCHEMY_DATABASE_URI```を```SQLALCHEMY_DATABASE_URL```と書いてたことでSQLALCHEMY_DATABASE_URIが指定されずにデフォルトのURI(sqlite:///:memory:)が指定されていた
- エラー文
```
UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".
  warnings.warn(
```
