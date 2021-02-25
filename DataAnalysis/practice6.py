# kaggleデータの取得(サイトからダウンロード)
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
from pprint import pprint
import pathlib

# 中間ディレクトリ(images)ごと作成
path_dir = pathlib.Path('images/survived')  # pathオブジェクト作成
path_dir.mkdir(parents=True, exist_ok=True)    # 中間ディレクトリ作成
print("\n'images/survived'ディレクトリ: ", path_dir.exists())

BASE_PATH = 'images/survived/'

# culumnsを全て表示する設定
pd.set_option('display.max_columns', None)

# データの読み込み
train_df = pd.read_csv('../TitanicML/titanic_data/train_private.csv')
test_df = pd.read_csv('../TitanicML/titanic_data/test_private.csv')

# print(train_df.head())
# print(test_df.head())
# print("\ntrain_df.columns = \n", train_df.columns)
# print("\ntest_df.columns = \n", test_df.columns)

# 訓練データの生存者と死亡者の人数を計算
survived = (train_df['Survived'] == 0).sum()
died = (train_df['Survived'] == 1).sum()
# print(survived, died)


# pandas
survived_series = pd.Series({'生存者数': survived, '死亡者数': died})
print(survived_series)
survived_series.plot(
    kind='pie',             # 円グラフ
    title='生存者割合',      # グラフタイトル
    startangle=90,          # 円グラフの始めを90°回転して上からプロット
    counterclock=False      # 反時計回りに出力(プロット)
)
# グラフを保存
plt.savefig(BASE_PATH + 'survived_pd_pie.png')
# グラフを表示
plt.show()

survived_series.plot(
    kind='bar',                 # 棒グラフ
    title='生存人数と死亡人数',
    rot=0                       # x軸のラベル名の回転を0°(なし)にする
)
plt.savefig(BASE_PATH + 'survived_pd_bar.png')
plt.show()


# matplotlib
# (辞書使用)
survived_dict = {'生存者数': survived, '死亡者数': died}
print(survived_dict.keys(), survived_dict.values())
# タイトル設定
plt.title('生存者割合')
# 円グラフ
plt.pie(
    x=survived_dict.values(),       # 値
    labels=survived_dict.keys(),    # ラベル
    counterclock=False,             # 反時計回りに出力(プロット)
    shadow=True,                    # 影を付ける
    startangle=90,                  # 円グラフの始めを90°回転して上からプロット
    autopct='%1.1f%%',              # 割合を%で表示
    explode=[0.1, 0]                # 最初の要素をグラフの中心から0.1離す
)
plt.savefig(BASE_PATH + 'survived_plt_pie.png')
plt.show()

plt.title('生存人数と死亡人数')
# 棒グラフ
plt.bar(
    x=survived_dict.keys(),         # x軸
    height=survived_dict.values(),  # y軸
    align='center'                  # 棒グラフの位置(x軸の値に対してグラフのどこを一致させるか)
)
# y軸ラベル
plt.ylabel('人数（人）')
plt.savefig(BASE_PATH + 'survived_plt_bar.png')
plt.show()

# ２つのグラフを横に並べて表示(辞書不使用)
# グラフのサイズ(２つ横に表示することを考慮してx(横)を広めの10に設定)
plt.figure(figsize=(10, 4))

# 縦１、横２のうちの１番目
plt.subplot(121)
plt.title('生存人数と死亡人数')
plt.bar(
    x=['生存者数', '死亡者数'],
    height=[survived, died],
    align='center'
)
plt.ylabel('人数（人）')

# 縦１、横２のうちの２番目
plt.subplot(122)
plt.title('生存者割合')
plt.pie(
    x=[survived, died],
    labels=['生存者数', '死亡者数'],
    counterclock=False,
    shadow=True,
    startangle=90,
    autopct='%1.1f%%',
    explode=[0.1, 0]
)

# グラフ全体のタイトル
plt.suptitle('Survived', fontsize=16)
plt.subplots_adjust(top=0.8)    # グラフの上に0.2のスペースを空ける
plt.savefig(BASE_PATH + 'survived_plt.png')
plt.show()


# seaborn
pprint(sns.get_dataset_names())
'''
['anagrams',
 'anscombe',
 'attention',
 'brain_networks',
 'car_crashes',
 'diamonds',
 'dots',
 'exercise',
 'flights',
 'fmri',
 'gammas',
 'geyser',
 'iris',
 'mpg',
 'penguins',
 'planets',
 'tips',
 'titanic']
'''
# data = sns.load_dataset('titanic')
# print(data)
# 訓練データの'Survived'カラムの要素(0, 1)ごとにカウントした値で棒グラフ作成
bar_graph = sns.countplot(x='Survived', data=train_df)
# 要素(0, 1)を['生存者数', '死亡者数']に変更
bar_graph.set_xticklabels(['生存者数', '死亡者数'])
# 一応、Seabornでもグラフの保存は出来るけどどうせmatplotlibのsavefig()メソッド
# を呼び出してるだけだから、以降はplt.savefig()を採用する
bar_graph.get_figure().savefig(BASE_PATH + 'survived_sns_bar.png')
plt.show()
