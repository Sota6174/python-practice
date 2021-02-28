import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pathlib
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

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
# print(df.head())

# 使用する特徴量に欠損値があるか確認
# print(df[['PassengerId', 'Pclass', 'Sex', 'Age', 'Embarked']].isnull().sum())
'''
PassengerId      0
Pclass           0
Sex              0
Age            263
Embarked         2
dtype: int64
'''

# 年齢の欠損値を補完する（今回は中央値で補完する）
# print("訓練データの年齢")
# print(f"平均：{train_df['Age'].mean().round(3)}歳, 中央値：{train_df['Age'].median()}歳")
'''
訓練データの年齢
平均：29.699歳, 中央値：28.0歳
'''
# print("テストデータの年齢")
# print(f"平均：{test_df['Age'].mean().round(3)}歳, 中央値：{test_df['Age'].median()}歳")
'''
テストデータの年齢
平均：30.273歳, 中央値：27.0歳
'''

df['Age'] = df['Age'].fillna(df['Age'].median())
# print(df[['Age']].isnull().sum())
'''
Age    0
dtype: int64
'''

# 港の欠損値を補完する（今回は一番多く人が乗り込んできたS(Southampton ship)で補完する）
df['Embarked'] = df['Embarked'].fillna('S')
# print(df[['Embarked']].isnull().sum())
'''
Embarked    0
dtype: int64
'''

# カラムを使うものだけに絞る
df = df.drop(columns=['Name', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin'])
# print(df.head())
'''
  PassengerId  Survived  Pclass     Sex   Age Embarked
0            1       0.0       3    male  22.0        S
1            2       1.0       1  female  38.0        C
2            3       1.0       3  female  26.0        S
3            4       1.0       1  female  35.0        S
4            5       0.0       3    male  35.0        S
'''
# print(df.isnull().sum())
'''
PassengerId      0
Survived       418  (testデータの分)
Pclass           0
Sex              0
Age              0
Embarked         0
dtype: int64
'''

# カテゴリカル変数を数値に変換
# 'Embarked'はワンホットエンコーディング：
# 'C' -> 'C' = 1, 'Q' = 0, 'S' = 0
# 'Q' -> 'C' = 0, 'Q' = 1, 'S' = 0
# 'S' -> 'C' = 0, 'Q' = 0, 'S' = 1
# 'Sex'はラベルエンコーディング：
# 'male', 'female'-> 0, 1

# # sklearnのモジュールで変換

# # 'Embarked'
# oe_encode = OneHotEncoder(sparse=False)
# values_nparray = oe_encode.fit_transform(df[['Embarked']].values)
# columns = oe_encode.get_feature_names(['Embarked'])
# # print(values_nparray)
# # print(columns)
# embarked_df = pd.DataFrame(values_nparray, columns=columns, dtype=int)
# # print(embarked_df)
# # 横方向に結合して、df['Embarked']は削除
# df = pd.concat([df, embarked_df], axis=1).drop(columns=['Embarked'])

# # 'Sex'
# le_encode = LabelEncoder()
# le_encode = le_encode.fit(df['Sex'])
# df['Sex'] = le_encode.transform(df['Sex'])
# print(df)

# pandasのget_dummies()メソッドで変換

# 'Embarked'
embarked_df = pd.get_dummies(df['Embarked'], prefix='Embarked')
# print(embarked_df)
# 横方向に結合して、df['Embarked']は削除
df = pd.concat([df, embarked_df], axis=1).drop(columns=['Embarked'])

# 'Sex'
df['Sex'] = pd.get_dummies(df['Sex'], drop_first=True)
# print(df)

# 訓練データとテストデータに分割する
# 'Survived'がNaNならテストデータ
train_df = df[~df['Survived'].isnull()]
test_df = df[df['Survived'].isnull()]
# print(f"train_df.shape: {train_df.shape}, test_df.shape: {test_df.shape}")
'''
train_df.shape: (891, 8), test_df.shape: (418, 8)
'''

# test_dfの'Survived'カラムを削除
test_df = test_df.drop(columns=['Survived'])
# print(test_df)

# train_dfのデータから学習する
