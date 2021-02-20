# python-practice

pythonで1日1つ何かしら作成していく

# 目的

- pythonで作りたいものを作れるようになる
- gitを使いこなせるようになる
- フレームワーク(Django, Flask)を使えるようになる
- データ解析出来るようになる
- API, Webスクレイピングが出来るようになる

# 期間

2021/02/10 ～ 2021/03/31

# 環境

- OS : Windows 10
- pythonバージョン : Python 3.9.1
- linter : flake8(pep8に準拠したコードを作成する)
- エディタ：VScode

# License
まだ、勉強中
- ライブラリのライセンス
- APIのライセンス

- clone, ダウンロードは自由にどうぞ!

# メモ

### Google Colaboratoryでpython3.9を動かすコード

```
!sudo add-apt-repository -y ppa:deadsnakes/ppa
!sudo apt-get -y update
!sudo apt-get -y install python3.9
!sudo apt-get -y install python3.9-dev
!sudo apt-get -y install python3-pip
!sudo apt-get -y install python3.9-distutils
!python3.9 -m pip install --upgrade setuptools
!python3.9 -m pip install --upgrade pip
!python3.9 -m pip install --upgrade distlib

!python3.9 -m pip install -r requirements.txt
!python3.9 test.py
```

- 参考: https://qiita.com/checche/items/396309459833e6ea598c

### 仮想環境でインストールしたモジュールを他の仮想環境でもインストールするときに使えるコマンド

1. requiments.txtを作成し、仮想環境内でインストールしたモジュールを書き出す
```
(venv1)> pip freeze > ./requirements.txt
```
2. 新しく作成した仮想環境(venv2)をアクティベートし、requirements.txtに書かれているモジュールをインストールする
```
(venv1)> deactivate
(base)> ./venv2/Scripts/activate
(venv2)> pip install -r ./requirements.txt
```
