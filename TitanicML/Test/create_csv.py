import pandas as pd

# データの読み込み
BASE_PATH = '../titanic_data/'
test_df = pd.read_csv(BASE_PATH + 'test_private.csv')

# 乗客のIDと性別のデータのみ抽出
test_df = test_df[['PassengerId', 'Sex']]

# 性別のデータから'Survived'の値(male->0(死亡), female->1(生存))を決定
print(test_df['Sex'] == 'male')
test_df.loc[test_df['Sex'] == 'male', 'Survived'] = 0
test_df.loc[test_df['Sex'] == 'female', 'Survived'] = 1
# 16行目の代入でNaNがあるため、0がfloat型で代入される
print(test_df)

# 提出用のcsvファイルにデータフレームのデータを書き込む
submission_df = test_df[['PassengerId', 'Survived']].astype(int)
# Seriesの型確認はdtype, DataFrameの型確認はdtypes
print(submission_df.dtypes)
# 'test.csv'にindexを消して書き込む
'''
to_csv()メソッドのデフォルト
index=True : インデックスも書き込む
header=True : ヘッダー（カラム名）も書き込む
mode='w' : 上書きモード、ファイルが無ければ新規作成)
encoding='utf-8' : 文字コードがutf-8で書き込まれる
columns=[] : 全てのカラムが書き込まれる、columnsでカラム名を指定すると指定されたカラムだけ書き込まれる
'''
submission_df.to_csv('test.csv', index=False)

# 提供されているgender_submission.csvと同じか確認
distribution_df = pd.read_csv(BASE_PATH + 'gender_submission_private.csv')
submission_df = pd.read_csv('test.csv')
check_df = (distribution_df != submission_df)
print(check_df)     # 一致してる場所はFalse, 一致していない場所はTrue
# 不一致(False)の件数をカウント
discrepancies_num = check_df.sum()
print("\n不一致(False)の件数\n", discrepancies_num)
