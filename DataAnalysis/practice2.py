# データ抽出の練習
import pandas as pd
pd.set_option('display.max_rows', 5)

df = pd.read_csv('data/japan_shiftjis.csv', encoding='shift-jis')
print(df)
print()

# スライス
print(df[:3])
print()
print(df[9:14])
print()
print(df[['人口（総数）']][:5])   # culumnsが人口（総数）のindex番号が0から4の値
print(df[['都道府県名', '人口（総数）']][:5])   # culumnsが都道府県名と人口（総数）のindex番号が0から4の値

# 真偽値
print(df[df['西暦（年）'] >= 2010])     # df['西暦（年）'] >= 2010がTrueのデータ
print(df[df['都道府県名'] == '東京都'])     # df['都道府県名'] == '東京都'がTrueのデータ
print(df[df['西暦（年）'] % 10 == 0])   # df['西暦（年）'] % 10 == 0がTrueのデータ
print(df[~(df['西暦（年）'] % 10 == 0)])   # df['西暦（年）'] % 10 == 0がFalseのデータ
print(df[df['西暦（年）'] % 10 != 0])   # df['西暦（年）'] % 10 != 0がTrueのデータ
print(df[(df['都道府県名'] == '東京都') & (df['西暦（年）'] == 2015)])
print(df[(df['都道府県名'] == '東京都') | (df['西暦（年）'] == 2015)])

# query()メソッド
# クエリに（）, ()は使えない
df = df.rename(columns={'西暦（年）': 'year'})
print(df.query('year == 2010'))

print(df.query('year > 2010'))
# print(df[df['year'] >= 2010]) と同じ

print(df.query('都道府県名 == ["東京都", "大阪府"]'))
print(df.query('都道府県名 in ["東京都", "大阪府"]'))
# print(df[df['都道府県名'] == '東京都']) と同じ

print(df.query('都道府県名 == "東京都" and year == 2015'))
# print(df[(df['都道府県名'] == '東京都') & (df['year'] == 2015)])と同じ

print(df.query('index > 900'))
print(df.loc[901:, :])

print(df.query('year % 10 == 0'))

# isin()メソッド
print(df[df['year'].isin([2010])])
# print(df[df['year'] == 2010]) と同じ
# print(df.query('year == 2010')) と同じ

print(df[df['year'].isin([2010, 2015])])
print(df[(df['year'] == 2010) | (df['year'] == 2015)])
print(df.query('year == [2010, 2015]'))

# 部分一致
print(df['都道府県名'].str.contains('山'))    # '山'を含む
print(df['都道府県名'].str.startswith('大'))    # '大'から始まる
print(df['都道府県名'].str.endswith('府'))  # '府'で終わる

# 抽出
print(df[df['year'] == df['year'].max()])
print(df[df['都道府県名'].isin(['北海道', '東京都'])].loc[:, ['人口（男）', '人口（女）']])
df_latest = df[df['year'] == df['year'].max()]
df_latest = df_latest.rename(columns={'人口（総数）': 'population'})
pd.set_option('display.max_rows', None)
print(df_latest[df_latest['population'] >= df_latest['population'].mean()].loc[:, ['都道府県名', 'population']])
