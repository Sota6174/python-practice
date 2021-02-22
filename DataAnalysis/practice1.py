import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df_japan_data = pd.read_csv('data/japan_shiftjis.csv', encoding='shift-jis')
print(df_japan_data.head(10))


tmp = df_japan_data[df_japan_data['都道府県名'] == '東京都']
tmp = tmp[['西暦（年）', '人口（男）', '人口（女）']]
tmp.plot.line(x='西暦（年）')
plt.show()

df_japan_data2 = pd.read_csv('data/japan_utf8.csv', encoding='UTF-8')
print(df_japan_data2.head(10))

tmp = df_japan_data2[df_japan_data2['都道府県名'] == '東京都']
tmp = tmp[['西暦（年）', '人口（男）', '人口（女）']]
tmp = tmp.rename(columns={'西暦（年）': 'year', '人口（男）': 'male', '人口（女）': 'female'})
tmp.plot.line(x='year')
plt.show()

tmp = df_japan_data[df_japan_data['都道府県名'] == '東京都']
tmp = tmp[['西暦（年）', '人口（男）', '人口（女）']]
tmp.plot.line(x='西暦（年）', figsize=(10, 6), title='東京の人口推移')
plt.savefig('images/pandas1.png')
plt.show()
