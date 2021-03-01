import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import pathlib
from sklearn import tree

# データの読み込み
BASE_PATH = '../titanic_data/'
train_df = pd.read_csv(BASE_PATH + 'train_private.csv')
test_df = pd.read_csv(BASE_PATH + 'test_private.csv')

# データを縦方向に連結（加工は同じ処理をするため）
df = pd.concat([train_df, test_df], ignore_index=True)

# 使用する特徴量に欠損値があるか確認
# print(df[['PassengerId', 'Pclass', 'Sex']].isnull().sum())
'''
PassengerId      0
Pclass           0
Sex              0
dtype: int64
'''

# カラムを使うものだけに絞る
df = df.drop(columns=['Name', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
# print(df.head())
'''
   PassengerId  Survived  Pclass     Sex
0            1       0.0       3    male
1            2       1.0       1  female
2            3       1.0       3  female
3            4       1.0       1  female
4            5       0.0       3    male
'''

# カテゴリカル変数を数値に変換
# 'Sex'はラベルエンコーディング：
# 'male', 'female'-> 0, 1

# pandasのget_dummies()メソッドで変換

# 'Sex'
df['Sex'] = pd.get_dummies(df['Sex'], drop_first=True)
# print(df.head())
'''
      PassengerId  Survived  Pclass  Sex
0               1       0.0       3    1
1               2       1.0       1    0
2               3       1.0       3    0
3               4       1.0       1    0
4               5       0.0       3    1
'''

# 訓練データとテストデータに分割する
# 'Survived'がNaNならテストデータ
train_df = df[~df['Survived'].isnull()]
test_df = df[df['Survived'].isnull()]
# print(f"train_df.shape: {train_df.shape}, test_df.shape: {test_df.shape}")
'''
train_df.shape: (891, 4), test_df.shape: (418, 4)
'''

# test_dfの'Survived'カラムを削除
test_df = test_df.drop(columns=['Survived'])
# print(test_df.head())
'''
      PassengerId  Pclass  Sex
891           892       3    1
892           893       3    0
893           894       2    1
894           895       3    1
895           896       3    0
'''

# train_dfのデータから学習する
# 今回はDecisionTreeClassifierで決定木モデルを作成する
y_train = train_df['Survived']                  # 小文字の'y' -> 値がベクトル
X_train = train_df.drop(columns=['Survived'])   # 大文字の'X' -> 値が行列

tree_clf = tree.DecisionTreeClassifier().fit(X_train, y_train)

# 作成したモデルを使ってtest_dfの'Survived'の値を予測する
y_prediction = tree_clf.predict(test_df)
# print(y_prediction)
'''
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 1. 1. 0. 0. 0. 0. 1. 0. 1. 1.
 1. 0. 1. 0. 1. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 1. 0. 1. 1. 0. 1. 0.
 1. 0. 1. 0. 1. 1. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 1. 1. 0. 1. 1. 1. 0. 0.
 0. 1. 1. 1. 0. 1. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 1. 0.
 1. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 1. 0. 0. 0. 1. 1.
 1. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0.
 1. 0. 1. 0. 1. 0. 1. 0. 0. 0. 0. 0. 1. 0. 1. 0. 0. 0. 1. 0. 0. 0. 1. 0.
 1. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 0. 1. 1. 0. 1. 0. 1. 0. 0. 0. 0. 1.
 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 1. 1. 0. 1. 0. 0. 1. 0. 0. 0. 0. 1. 0. 1.
 0. 1. 1. 0. 1. 0. 1. 0. 1. 0. 0. 0. 0. 0. 0. 1. 0. 0. 1. 0. 1. 0. 1. 1.
 1. 1. 1. 0. 0. 1. 1. 0. 1. 0. 1. 0. 1. 0. 0. 0. 0. 0. 1. 0. 0. 0. 1. 0.
 0. 0. 1. 0. 0. 0. 1. 0. 1. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1.
 0. 0. 1. 0. 0. 1. 0. 0. 1. 0. 1. 0. 0. 0. 0. 0. 0. 1. 1. 0. 1. 0. 0. 0.
 0. 0. 1. 0. 1. 0. 0. 0. 0. 0. 0. 1. 1. 0. 1. 1. 0. 0. 1. 1. 0. 0. 0. 1.
 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 1. 1. 0. 0. 0. 0. 1. 1. 0. 0. 0.
 0. 1. 1. 0. 1. 0. 0. 0. 1. 0. 0. 1. 1. 0. 1. 1. 0. 0. 1. 0. 0. 0. 0. 0.
 0. 1. 0. 0. 0. 0. 1. 1. 0. 0. 0. 1. 0. 1. 0. 0. 1. 0. 1. 1. 1. 0. 0. 1.
 0. 0. 0. 1. 0. 0. 1. 0. 0. 0.]
'''
# print(len(test_df), len(y_prediction))
'''
418 418
'''

# 予測結果をtest_dfに反映
test_df['Survived'] = y_prediction
# print(test_df.head())
'''
     PassengerId  Pclass  Sex  Survived
891          892       3    1       0.0
892          893       3    0       0.0
893          894       2    1       0.0
894          895       3    1       0.0
895          896       3    0       0.0
'''

# 提出用のcsvファイルにデータフレームのデータを書き込む
submission_df = test_df[['PassengerId', 'Survived']].astype(int)
# Seriesの型確認はdtype, DataFrameの型確認はdtypes
print(submission_df.dtypes)
'''
PassengerId    int32
Survived       int32
dtype: object
'''
# 'test.csv'にindexを消して書き込む
submission_df.to_csv('method1_2.csv', index=False)

# 'method1.csv'の予測値との違いを確認
method1_df = pd.read_csv('method1.csv')
method1_2_df = pd.read_csv('method1_2.csv')
check_df = (method1_df != method1_2_df)
# print(check_df)     # 一致してる場所はFalse, 一致していない場所はTrue
# 不一致(False)の件数をカウント
discrepancies_num = check_df['Survived'].sum()
# print("\n不一致(False)の件数: ", discrepancies_num)
'''
不一致(False)の件数:  98
'''
