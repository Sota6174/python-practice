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
test_df = pd.read_csv(BASE_PATH + 'test_private.csv')

# データを縦方向に連結（加工は同じ処理をするため）
# ignore_index=Trueでindex番号を0から振り直す
df = pd.concat([train_df, test_df], ignore_index=True)
print(df.head())
