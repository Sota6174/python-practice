# Titanic

- データサイエンスの練習をする

# 目標

- kaggleの[Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview)でTrainデータから、Titanic号の乗客で生存する人の特徴、生存フラグとの相関を探し出し、Testデータの乗客が生存するか予測する
- 2月中にScore0.9以上を出す(1.0で全部一致)

# 学習手順

1. データサイエンスの流れを実際にコードを書きながら勉強する
2. 動画で扱っていないデータ項目についても、pandas・matplotlib・seabornの練習も兼ねて、可視化する
3. 可視化したデータから、仮説を立てる(isuueを立てて記載していく)
4. 自分なりの学習モデルを作成し、検証する

# 環境

- 学習手順の１～３はGoogleColaboratoryを使用する
- 学習手順４はローカル環境かGoogleColaboratoryか考え中

# 参考動画

- [はやたす / Pythonエンジニア](https://www.youtube.com/watch?v=F3D75T_wW4w&list=PL4Y-mUWLK2t0Vy2sUIXK3ItMX0s7CvoB_)さんの動画
- [キノコード / プログラミング学習チャンネル](https://www.youtube.com/c/kinocode/featured)さんの動画

# メモ

### GoogleColaboratoryのセル全実行コマンド

- Windows: Ctrl + F9
- Mac: cmd + F9

### 欠損値の保管

- データの欠損値は削除か補完で対応する

### カテゴリカル変数は数値変換する

- A, B, C -> 0, 1, 2 (ラベルエンコーディング)
- True(Yes), False(No) -> 1, 0 (ワンホットエンコーディング)