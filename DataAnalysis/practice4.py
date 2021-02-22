# csvファイル, Excelファイルの読み込み, 加工, 保存
# Excelファイルは1つのファイルで複数sheet保存出来る
import pandas as pd
pd.set_option('display.max_rows', 5)

df_1 = pd.read_csv('data/japan_shiftjis.csv', encoding='shift-jis')
print(df_1)

# sheetを複数に分けて保存するときは、pd.ExcelWriter()を用い、書き出しが終わったらExcelファイルを閉じる
# デフォルトで上書き(mode='w')
with pd.ExcelWriter('data/japan_shiftjis.xlsx') as writer:

    # そのまま書き出し
    df_1.to_excel(writer, sheet_name='japan1')

    # index番号を消して書き出し
    df_1.to_excel(writer, sheet_name='japan1_noindex', index=False)

    # '都道府県名', '西暦（年）', '人口（総数）'の列だけ書き出し
    df_2 = df_1.loc[:, ['都道府県名', '西暦（年）', '人口（総数）']]
    df_2.to_excel(writer, sheet_name='japan2', index=False)

    # '都道府県名', '西暦（年）', '人口（総数）'の列の値だけ書き出し
    df_2.to_excel(
        writer,
        sheet_name='japan2_noheader',
        index=False,
        header=False)

    # '都道府県コード', '都道府県名', '人口（総数）'を人口（総数）の降順(多い順)で書き出し
    # ascending: デフォルト(True)で昇順(a->z, あ->ん, 0->∞)
    df_3 = df_1[df_1['西暦（年）'] == df_1['西暦（年）'].max()]
    df_3 = df_3.set_index('都道府県コード')
    df_3.sort_values(by='人口（総数）', ascending=False, inplace=True)
    df_3.to_excel(writer, sheet_name='japan3')

# axis=1は列で並び替え(デフォルトでaxis=0)[0, 1: 行（縦）, 列（横）]
print(df_3.query('都道府県名 == ["北海道", "東京都", "沖縄県"]').index)
print(df_3.query('都道府県名 == ["北海道", "東京都", "沖縄県"]').index.values)
print(type(df_3.query('都道府県名 == ["北海道", "東京都", "沖縄県"]').index.values))
drop_list = df_3.query('都道府県名 == ["北海道", "東京都", "沖縄県"]').index.values.tolist()
df_4 = df_3.drop(drop_list)
df_4 = df_4.drop(['元号', '和暦（年）', '西暦（年）', '人口（男）', '人口（女）'], axis=1)
print(df_4)
df_5 = pd.DataFrame({'都道府県名': ['北海道', '東京都', '沖縄県']}, index=drop_list)
print(df_5)

# 既にあるExcelファイルに書き足す場合(appendモード)
with pd.ExcelWriter('data/japan_shiftjis.xlsx', mode='a') as writer:
    df_nan = pd.concat([df_4, df_5])
    print(df_nan)
    df_nan.to_excel(writer, sheet_name='japan_nan')
