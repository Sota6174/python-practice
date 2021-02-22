# データのsort
# 漢字は、昇順・降順で並び替えない方がいい
# SeriesもDetaFrameと同じように並び替え可能
import pandas as pd
pd.set_option('display.max_rows', 15)

df_1 = pd.read_excel(
    'data/japan_shiftjis.xlsx',
    sheet_name='japan1',
    index_col=0)
print(df_1)

# '都道府県コード'で降順(False)、'西暦（年）'で昇順(True)に並び替え
df_1 = df_1.sort_values(by=['都道府県コード', '西暦（年）'], ascending=[False, True])
print(df_1)
# index番号の振り直し
df_1 = df_1.reset_index()
print(df_1)

# 東京都のデータを抽出
df_tokyo = df_1[df_1['都道府県名'] == '東京都']
print(df_tokyo)

# '人口（総数）'で降順(False)に並び替え
df_tokyo = df_tokyo.sort_values(by='人口（総数）', ascending=False)
print(df_tokyo)

# '西暦（年）'で昇順(True)に並び替え
df_tokyo = df_tokyo.sort_values(by='西暦（年）')
print(df_tokyo)

df_2 = pd.read_excel(
    'data/japan_shiftjis.xlsx',
    sheet_name='japan3',
    index_col=0)
print(df_2)

df_2 = df_2.drop(['元号', '和暦（年）', '西暦（年）'], axis=1)
print(df_2)

# indexで昇順に並び替え
df_2 = df_2.sort_index()
print(df_2)

# 全てのsheetをまとめて読み込む場合
df_allsheet = pd.read_excel('data/japan_shiftjis.xlsx', sheet_name=None)
print(df_allsheet.keys())
