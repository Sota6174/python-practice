# csvファイル, Excelファイルの読み込み, 加工, 保存
# Excelファイルは1つのファイルで複数sheet保存出来る
import pandas as pd
pd.set_option('display.max_rows', 5)


df_1 = pd.read_csv('data/japan_shiftjis.csv', encoding='shift-jis')
print(df_1)
df_2 = df_1.loc[:, ['都道府県名', '西暦（年）', '人口（総数）']]
print(df_2)

df_2.to_csv('data/japan2_shiftjis.csv', encoding='shift-jis', index=False)
df_1.to_excel('data/japan_shiftjis.xlsx', sheet_name='japan', index=False)
