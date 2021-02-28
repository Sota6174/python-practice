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
sns.set(font='IPAexGothic', font_scale=0.9)

# # 性別に関するグラフを３つ横に並べて表示
# plt.figure(figsize=(13, 5))

# # 男女の人数
# plt.subplot(131)
# plt.title('男女の人数')
# sns.countplot(data=train_df, x='Sex')
# plt.xlabel('性別')
# plt.ylabel('人数')
# # print(plt.xticks())
# # (array([0, 1]), [Text(0, 0, 'male'), Text(1, 0, 'female')])
# plt.xticks([0, 1], ['男性', '女性'])

# # 男女ごとの生存・死亡人数
# plt.subplot(132)
# plt.title('男女ごとの生存・死亡人数')
# sns.countplot(data=train_df, x='Sex', hue='Survived')
# plt.xlabel('性別')
# plt.ylabel('人数')
# plt.legend(labels=['死亡者数', '生存者数'], fontsize=8)
# plt.xticks([0, 1], ['男性', '女性'])

# # 男女ごとの生存率
# plt.subplot(133)
# plt.title('男女ごとの生存率')
# # ci=Noneで信頼区間を表すエラーバーを非表示にする
# sns.barplot(data=train_df, x='Sex', y='Survived', ci=None)
# plt.xlabel('性別')
# plt.ylabel('生存率')
# plt.xticks([0, 1], ['男性', '女性'])

# # グラフ全体の設定
# plt.suptitle('性別に関するグラフ', fontsize=15)
# # グラフの上に0.2、左に0.1、右に0.05、グラフ同士の間に0.3のスペースを空ける
# plt.subplots_adjust(top=0.8, left=0.1, right=0.95, wspace=0.3)
# plt.savefig('images/sex2.png')
# plt.show()

# # チケットのクラスに関するグラフを３つ横に並べて表示
# plt.figure(figsize=(16, 5))

# # チケットのクラスごとの人数
# plt.subplot(131)
# plt.title('クラスごとの人数')
# sns.countplot(data=train_df, x='Pclass')
# plt.xlabel('クラス')
# plt.ylabel('人数')

# # チケットのクラスごとの生存・死亡人数
# plt.subplot(132)
# plt.title('クラスごとの生存・死亡人数')
# sns.countplot(data=train_df, x='Pclass', hue='Survived')
# plt.xlabel('クラス')
# plt.ylabel('人数')
# plt.legend(labels=['死亡者数', '生存者数'], fontsize=8)

# # チケットのクラスごとの生存率
# plt.subplot(133)
# plt.title('クラスごとの生存率')
# # ci=Noneで信頼区間を表すエラーバーを非表示にする
# sns.barplot(data=train_df, x='Pclass', y='Survived', ci=None)
# plt.xlabel('クラス')
# plt.ylabel('生存率')

# # グラフ全体の設定
# plt.suptitle('チケットのクラスに関するグラフ', fontsize=15)
# # グラフの上に0.2、左に0.1、右に0.05、グラフ同士の間に0.3のスペースを空ける
# plt.subplots_adjust(top=0.8, left=0.1, right=0.95, wspace=0.3)
# plt.savefig('images/pclass2.png')
# plt.show()

# # 年齢の人数に関するグラフを２つ横に並べて表示
# # 年齢のデータには欠損値がある
# # print("年齢データの欠損値の数: ", train_df['Age'].isnull().sum())
# # 年齢データの欠損値の数:  177

# # ここでは欠損値は削除して可視化
# age_df = train_df.dropna(subset=['Age'])
# # print(age_df.shape)
# # (714, 12) : 714 = 891 - 177

# plt.figure(figsize=(12, 5))

# # 年齢層ごとの人数
# plt.subplot(121)
# plt.title('年齢層ごとの人数')
# # ヒストグラムを作成するときにdistplot()を使うと非推奨を言われる
# # displot()を使うとplt.subplot()で指定しても、それぞれ別々の画面にヒストグラムのグラフが表示されてしまう
# # カーネル密度推定（KDE）：kde=Trueで確率密度関数も表示
# sns.histplot(data=age_df, x='Age', kde=True)
# plt.xlabel('年齢層')
# plt.ylabel('人数')

# # 年齢層ごとの生存・死亡人数
# plt.subplot(122)
# plt.title('年齢層ごとの生存・死亡人数')
# sns.histplot(data=age_df, x='Age', hue='Survived', multiple='stack')
# plt.xlabel('年齢層')
# plt.ylabel('人数')
# plt.legend(labels=['生存者数', '死亡者数'], fontsize=8)

# # グラフ全体の設定
# plt.suptitle('年齢に関するグラフ')
# # グラフの上に0.2、グラフ同士の間に0.3のスペースを空ける
# plt.subplots_adjust(top=0.8, wspace=0.3)
# plt.savefig('images/age.png')
# plt.show()

# # 確認用
# tmp_df = age_df[age_df['Age'] < 5][['Age', 'Survived']]
# print(f"5歳未満死亡{tmp_df[tmp_df['Survived'] == 0].shape}人")
# # (13, 2)：5歳未満13人死亡
# print(f"5歳未満生存{tmp_df[tmp_df['Survived'] == 1].shape}人")
# # (27, 2)：5歳未満27人死亡

# チケットのクラスに関するグラフを２つ横に並べて表示
# 港のデータには欠損値がある
# print("港データの欠損値の数: ", train_df['Embarked'].isnull().sum())
# 港データの欠損値の数:  2

plt.figure(figsize=(12, 5))

# 港ごとの人数
plt.subplot(131)
plt.title('港ごとの人数')
sns.countplot(data=train_df, x='Embarked')
plt.xlabel('港')
plt.ylabel('人数')
# print(plt.xticks())
'''
(
    array([0, 1, 2]),
    [Text(0, 0, 'S'),
    Text(1, 0, 'C'),
    Text(2, 0, 'Q')]
)
'''
plt.xticks([0, 1, 2], ['Southampton', 'Cherbourg', 'Queenstown'])


# 港のクラスごとの生存・死亡人数
plt.subplot(132)
plt.title('港ごとの生存・死亡人数')
sns.countplot(data=train_df, x='Embarked', hue='Survived')
plt.xlabel('港')
plt.ylabel('人数')
plt.legend(labels=['死亡者数', '生存者数'], fontsize=8)
plt.xticks([0, 1, 2], ['Southampton', 'Cherbourg', 'Queenstown'])

# 港ごとの生存率
plt.subplot(133)
plt.title('港ごとの生存率')
# ci=Noneで信頼区間を表すエラーバーを非表示にする
sns.barplot(data=train_df, x='Embarked', y='Survived', ci=None)
plt.xlabel('港')
plt.ylabel('生存率')
plt.xticks([0, 1, 2], ['Southampton', 'Cherbourg', 'Queenstown'])

# グラフ全体の設定
plt.suptitle('港に関するグラフ', fontsize=15)
# グラフの上に0.2、左に0.1、右に0.05、グラフ同士の間に0.3のスペースを空ける
plt.subplots_adjust(top=0.8, left=0.1, right=0.95, wspace=0.3)
plt.savefig('images/embarked.png')
plt.show()
