# DiscodeBot

- Discode内で使えるBotを作ってみる

# 環境

- 

# メモ

### python3.9.1はdiscode.pyをインストール出来ない
'''
(py39-venv) > pip install discode.py
ERROR: Could not find a version that satisfies the requirement discode.py (from versions: none)
ERROR: No matching distribution found for discode.py
'''

### そもそも仮想環境でdiscode.pyをインストール出来なかった
'''
(py38-venv) > py -V
Python 3.8.2
(py38-venv) > pip install discode.py
ERROR: Could not find a version that satisfies the requirement discode.py
ERROR: No matching distribution found for discode.py
'''
- [この記事](https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f)では3.8.2の環境でやっている

### python3.9.1はdiscode.pyをインストール出来ない訳ではなかった
'''
\> py -V
Python 3.9.1
\> py -m pip install -U discord.py
'''
- Python 3.9.1の環境でもローカルの環境にインストールすることは出来た
- ローカルの環境なら'''\> pip install discord.py'''でもインストール出来た
