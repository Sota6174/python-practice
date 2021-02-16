# WebAppPrimer

- pythonとFlaskでWebアプリを作成する
- 表示の見た目を整えるのにBootstrapをダウンロードし使用した
- 仮想環境フォルダとダウンロードしたstatic/cssフォルダはリモート上の管理から除外済み

# 仮想環境の構築

- [Issueのリンク](https://github.com/Sota6174/python-practice/issues/6#issue-807942767)

# フレームワークを使用する環境を仮想環境内に構築する

- https://proengineer.internous.co.jp/content/columnfeature/15156
- 今回はFlaskを用いる
- モジュールのインポート
  - ```pip install flask flask-sqlalchemy```

# Bootstrapを使用する環境の構築

- ローカル環境にBootstrapを使うためのファイルをダウンロードして使用する
1. https://getbootstrap.jp/ にアクセスし、ローカル環境にBootstrapをダウンロードし、zipファイルを展開する
2. bootstrap-5.0.0-beta1-distフォルダのcssファイルのみをstaticフォルダ内にコピーする
3. base.html内の8行目のようにローカルで保存しているパスを指定してhtmlに埋め込む

- [Bootstrap CDN](https://getbootstrap.jp/docs/4.3/getting-started/introduction/)を利用してBootstrapを使うためのファイルをダウンロードせずに使用する
1. Bootstrap CDNを利用してbase2.html内の8行目のようにhtmlに埋め込む

# ローカル環境でのテスト実行時

0. dbを作成する(todo.dbが作られればOK)
```
> py
>>> from test4 import db
>>> db.create_all()
>>> quit()
```
1. ターミナルで```py test4.py```などファイルを実行する
2. Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)と言われるので、http://127.0.0.1:5000/ に飛ぶ

# 作成したtodoアプリを公開

- データベースの内容を更新したりなどの動的な処理があるため、github pagesではなく、Herokuを用いて、デプロイする
- [デプロイ・ビルド・リリースの違い](https://engineer-club.jp/deploy)
1. [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)のインストール
2. 仮想環境にgunicornをインストール
  - ```> pip install gunicorn```
3. requirements.txtにgunicornを追加
  - ```> pip freeze > .\requirements.txt```
4. [Procfile](https://devcenter.heroku.com/ja/articles/getting-started-with-python#procfile)を作成し、中に"web: gunicorn app:app --log-file=-"を記載
  - ```> touch ./Procfile```
  - ```> echo "web: gunicorn app:app --log-file=-" > ./Procfile```
5. gitリポジトリを作成
  - ```> git init```
  - ```> git add .```
  - ```> git commit -m "コミットメッセージ"```
6. Herokuにログイン
  - ```> heroku login```
  - Herokuのログインページに飛ぶため、そこでログインする
7. アプリを作成
  - ```> heroku create アプリ名```
  - アプリ名の部分は、そのままURLに使われるため、他のアプリと重複していると、その名前は使えない(=ユニークな名前にする必要がある)
8. アプリを公開する
  - ```> git push heroku master```
9. アプリのURL(https://アプリ名.herokuapp.com/)にアクセスする


# 参考動画

- [はやたす / Pythonエンジニア](https://www.youtube.com/watch?v=9JDFVEur0Xs&list=PL4Y-mUWLK2t2rISQza73yNiz6_8HTaQiY&index=23)さんの動画

# モジュールのインポート

- repuirements.txtに記載

# メモ

### 実行時の0番でエラーを出された

- 原因は```SQLALCHEMY_DATABASE_URI```を```SQLALCHEMY_DATABASE_URL```と書いてたことでSQLALCHEMY_DATABASE_URIが指定されずにデフォルトのURI(sqlite:///:memory:)が指定されていた
- エラー文
```
UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".
  warnings.warn(
```

### [Bootstrap CDN](https://getbootstrap.jp/docs/4.3/getting-started/introduction/)について

- [CDN](https://www.kagoya.jp/howto/network/cdn/)：Content Delivery Networkの略
- CDNではウェブコンテンツ配信用にネットワークを最適化する(オリジンサーバーではなく、代理サーバー(=キャッシュサーバー)にアクセスを向ける)ことによって、アクセスが集中したりコンテンツが大容量化したりしても、ホームページの表示やコンテンツの配信に問題が起こらないようにすることが可能
- キャッシュサーバーにアクセスを向けることで、サーバーやネットワークにかかる負荷を分散出来る
