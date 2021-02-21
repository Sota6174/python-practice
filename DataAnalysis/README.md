# DataAnalysis

- pythonのデータ解析で頻繁に使われるモジュール(pandas/Matplotlib/Seaborn)を使えるようになる

# 目標

- モジュールそれぞれでkaggleの[Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview)のTrainデータを可視化する

# 仮想環境の構築

- [Issueのリンク](https://github.com/Sota6174/python-practice/issues/6#issue-807942767)


# 参考動画

- [キノコード / プログラミング学習チャンネル](https://www.youtube.com/c/kinocode/featured)さんの動画

# モジュールのインポート

- repuirements.txtに記載

# メモ

### 日本語の文字化け(豆腐バグ)

- グラフで日本語を表示しようとすると、文字化けし、▯▯▯▯▯▯▯のように表示される
- 以下は豆腐回避手順

1. japanize-matplotlibモジュールをインストールする
- VScode: ```> pip install japanize-matplotlib```
- Google Colabotatory: ```!pip install japanize-matplotlib```

2. コード内で```import japanize_matplotlib```と記載する
