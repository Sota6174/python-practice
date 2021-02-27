import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pathlib

# imagesディレクトリ作成
path_dir = pathlib.Path('images')  # pathオブジェクト作成
path_dir.mkdir(parents=True, exist_ok=True)    # ディレクトリ作成

# データの読み込み
BASE_PATH = '../titanic_data/'
train_df = pd.read_csv(BASE_PATH + 'train_private.csv')
test_df = pd.read_csv(BASE_PATH + 'test_private.csv')

# データフレームの基本情報の確認
# print("\ntrain_df\n" + "*" * 30)
# print("shape: ", train_df.shape)
# print("\nhead: \n", train_df.head())
# print("\ncolumns: \n", train_df.columns)
# print("\n欠損値の数: \n", train_df.isnull().sum())
# print("\n基本統計量: \n", train_df.describe())
# print("*" * 30 + "\n")

# print("\ntest_df\n" + "*" * 30)
# print("shape: ", test_df.shape)
# print("\nhead: \n", test_df.head())
# print("\ncolumns: \n", test_df.columns)
# print("\n欠損値の数: \n", test_df.isnull().sum())
# print("\n基本統計量: \n", test_df.describe())
# print("*" * 30 + "\n")

# data_info.txtファイルに情報を書き足す(ファイルが無ければ新規作成される)
with open(BASE_PATH + 'data_info.txt', mode='a', encoding='utf-8') as f:
    f.write("\ntrain_df\n" + "*" * 60 + "\n")
    f.write(f"shape: {train_df.shape}\n\n")
    f.write(f"head: \n{train_df.head()}\n\n")
    f.write(f"columns: \n{train_df.columns}\n\n")
    f.write(f"欠損値の数: \n{train_df.isnull().sum()}\n\n")
    f.write(f"基本統計量: \n{train_df.describe()}\n\n")
    f.write("*" * 60 + "\n\n")

    f.write("\ntest_df\n" + "*" * 60 + "\n")
    f.write(f"shape: {test_df.shape}\n\n")
    f.write(f"head: \n{test_df.head()}\n\n")
    f.write(f"columns: \n{test_df.columns}\n\n")
    f.write(f"欠損値の数: \n{test_df.isnull().sum()}\n\n")
    f.write(f"基本統計量: \n{test_df.describe()}\n\n")
    f.write("*" * 60 + "\n")

# 男女の人数
data_sex = train_df.groupby('Sex').agg({'Sex': 'count'})
data_sex = data_sex.rename(columns={'Sex': 'count_sex'})
print(data_sex)

# データの可視化(グラフ)
# Seabornのデフォルトスタイルを設定(fontを設定しないと文字化けする)
sns.set(font='IPAexGothic')
# 男女の人数
plt.title('男女の人数')
sns.countplot(x='Sex', data=train_df)
plt.xlabel('性別')
plt.ylabel('人数')
plt.savefig('images/sex.png')
plt.show()

# 男女ごとの生存率(Seaborn)
plt.title('男女ごとの生存率')
# ci=Noneで信頼区間を表すエラーバーを非表示にする
sns.barplot(x='Sex', y='Survived', ci=None, data=train_df)
plt.xlabel('性別')
plt.ylabel('生存率')
plt.savefig('images/survival_rate.png')
plt.show()
