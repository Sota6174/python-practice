import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pathlib

# imagesディレクトリ作成
path_dir = pathlib.Path('images')
path_dir.mkdir(exist_ok=True)

# データの読み込み
BASE_PATH = '../titanic_data/'
train_df = pd.read_csv(BASE_PATH + 'train_private.csv')

# データの可視化
# Seabornのデフォルトスタイルを設定(fontを設定しないと文字化けする)
sns.set(font='IPAexGothic')

# 男女の人数に関するグラフを２つ横に並べて表示
plt.figure(figsize=(10, 4))

# 男女の人数
plt.subplot(121)
plt.title('男女の人数')
sns.countplot(x='Sex', data=train_df)
plt.xlabel('性別')
plt.ylabel('人数')
# print(plt.xticks())
# (array([0, 1]), [Text(0, 0, 'male'), Text(1, 0, 'female')])
plt.xticks([0, 1], ['男性', '女性'])

# 男女ごとの生存率
plt.subplot(122)
plt.title('男女ごとの生存率')
# ci=Noneで信頼区間を表すエラーバーを非表示にする
sns.barplot(x='Sex', y='Survived', ci=None, data=train_df)
plt.xlabel('性別')
plt.ylabel('生存率')
plt.xticks([0, 1], ['男性', '女性'])

# グラフ全体の設定
plt.suptitle('男女の人数に関するグラフ')
# グラフの上に0.2、グラフの間に0.3のスペースを空ける
plt.subplots_adjust(top=0.8, wspace=0.3)
plt.savefig('images/sex.png')
plt.show()

# チケットのクラスに関するグラフを２つ横に並べて表示
plt.figure(figsize=(11, 4))

# チケットのクラスごとの人数
plt.subplot(121)
plt.title('クラスごとの人数')
sns.countplot(x='Pclass', data=train_df)
plt.xlabel('クラス')
plt.ylabel('人数')

# チケットのクラスごとの生存率
plt.subplot(122)
plt.title('クラスごとの生存率')
# ci=Noneで信頼区間を表すエラーバーを非表示にする
sns.barplot(x='Pclass', y='Survived', ci=None, data=train_df)
plt.xlabel('クラス')
plt.ylabel('生存率')

# グラフ全体の設定
plt.suptitle('チケットのクラスに関するグラフ', fontsize=15)
# グラフの上に0.2、グラフの間に0.3のスペースを空ける
plt.subplots_adjust(top=0.8, wspace=0.3)
plt.savefig('images/pclass.png')
plt.show()

# 年齢ごとの人数
# 年齢のデータには欠損値がある
# print("年齢データの欠損値の数: ", train_df['Age'].isnull().sum())
# 年齢データの欠損値の数:  177

# ここでは欠損値は削除して可視化
age_df = train_df.dropna(subset=['Age'])
# print(age_df.shape)
# (714, 12) : 714 = 891 - 177

# 年齢ごとの人数
# ヒストグラムを作成するときにdistplot()を使うと非推奨を言われる
sns.displot(data=age_df, x='Age')
plt.xlabel('年齢')
plt.ylabel('人数')
# print(plt.xticks())
'''
(array([-10.,   0.,  10.,  20.,  30.,  40.,  50.,  60.,  70.,  80.,  90.]),
    [Text(-10.0, 0, '−10'), Text(0.0, 0, '0'),
    Text(10.0, 0, '10'), Text(20.0, 0, '20'),
    Text(30.0, 0, '30'), Text(40.0, 0, '40'),
    Text(50.0, 0, '50'), Text(60.0, 0, '60'),
    Text(70.0, 0, '70'),
    Text(80.0, 0, '80'),
    Text(90.0, 0, '90')]
)
'''
plt.show()
