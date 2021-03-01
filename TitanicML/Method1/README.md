# Method1

- [はやたす / Pythonエンジニア](https://www.youtube.com/watch?v=F3D75T_wW4w&list=PL4Y-mUWLK2t0Vy2sUIXK3ItMX0s7CvoB)さんの動画で紹介されていた手法

# 手順

1. データを読み込む
2. 訓練データをテストデータを結合
3. データの欠損値を補完
4. 文字列データを数値にエンコード
5. 加工したデータフレームを訓練データとテストデータに分割
6. 決定木分析で訓練データからモデル作成
7. 作成したモデルでテストデータの'Survived'の値を予測
8. 提出用のcsvファイルを作成する

# Score(全部一致で1.0)
- 0.71531

# 考察
- チケットのクラス(Pclass)
    - 一番ランクの低いチケットの人数が一番多く、次に一番ランクの高いチケットの人数が多い
    - チケットのランクが高いほど生存率が高い
- 性別(Sex)
    - 男性の方が多く乗っている
    - 女性の方が生存率が高い
- 年齢(Age)
    - 20～30代が一番多い
    - 生存率が5歳以下は高そうだと感じるが、あまり年齢と生存率に関係はなさそう
- タイタニック号に乗った港(Embarked)
    - 'S'から乗った人が一番多い
    - 'C'から乗った人の生存率が一番高いが、それでも0.56くらいで男女比がそのまま影響を与えていそう

# 感想

- Pclass, Sex, Age, EmbarkedのデータごとにSurvivedとどんな相関があるのかはグラフで可視化することである程度分かったが、それをモデル作成に活かすことが出来なかった
- Age, Embarkedのデータは生存とあまり関係なさそうだと思い、create_csv2.pyで試してみたら予想通りScoreは変わらなかった（全く同じScoreになるとは思っていなかった）

# メモ

### 決定木分析とは
- https://qiita.com/3000manJPY/items/ef7495960f472ec14377
- https://hira03.hatenablog.com/entry/DecisionTreeClassifier_DecisionTreeRegressor

### plt.subplots_adjust()について

- デフォルト値
> left  = 0.125  # the left side of the subplots of the figure
> right = 0.9    # the right side of the subplots of the figure
> bottom = 0.1   # the bottom of the subplots of the figure
> top = 0.9      # the top of the subplots of the figure
> wspace = 0.2   # the amount of width reserved for space between subplots,
>                # expressed as a fraction of the average axis width
> hspace = 0.2   # the amount of height reserved for space between subplots,
>                # expressed as a fraction of the average axis height
