# Titanic

- データサイエンスの練習をする

# 目標

- kaggleの[Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview)でTrainデータから、Titanic号の乗客で生存する人の特徴、生存フラグとの相関を探し出し、Testデータの乗客が生存するか予測する
- 2月中にScore0.9以上を出す(1.0で全部一致)

# 学習手順

1. データサイエンスの流れを実際にコードを書きながら勉強する
2. 動画で扱っていないデータ項目についても、pandas・matplotlib・seabornの練習も兼ねて、可視化する
3. いろいろなサイト・動画を見て、学習モデルの作成にどんなことをしなければいけないのか、データからどのように特徴を見つけ出すのか、考え方・基準を学びながら、自分の環境でコードを書いてみる

# 環境

- VScode上で[仮想環境を構築](https://github.com/Sota6174/python-practice/issues/6#issue-807942767)する
- 使用した外部ライブラリはRequirements.txtに記載する
- 学習モデルの作成に必要だと感じたデータの可視化はtest.pyで行い、提出するcsvファイルの作成はcreate_csv.pyファイルで行う

# メモ

### GoogleColaboratoryのセル全実行コマンド

- Windows: Ctrl + F9
- Mac: cmd + F9

### 欠損値の保管

- データの欠損値は削除か補完で対応する

### カテゴリカル変数は数値変換する

- A, B, C -> 0, 1, 2 (ラベルエンコーディング)
- True(Yes), False(No) -> 1, 0 (ワンホットエンコーディング)

### データの可視化

- [train.csv](https://www.kaggle.com/c/titanic/data?select=train.csv)の各項目のデータはサイト上のDetailで可視化されている

### kaggle api

- [githubリンク]https://github.com/Kaggle/kaggle-api)
- [ドキュメント]https://www.kaggle.com/docs/api)
