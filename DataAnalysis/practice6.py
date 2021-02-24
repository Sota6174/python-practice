# kaggleデータの取得(サイトからダウンロード)
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
from pprint import pprint

pd.set_option('display.max_columns', None)

train_df = pd.read_csv('../TitanicML/titanic_data/train_private.csv')
test_df = pd.read_csv('../TitanicML/titanic_data/test_private.csv')

# print(train_df.head())
# print(test_df.head())
# print("\ntrain_df.columns = \n", train_df.columns)
# print("\ntest_df.columns = \n", test_df.columns)

survived = (train_df['Survived'] == 0).sum()
died = (train_df['Survived'] == 1).sum()
# print(survived, died)


# pandas
survived_series = pd.Series({'生存者数': survived, '死亡者数': died})
print(survived_series)
survived_series.plot(
    kind='pie',
    title='生存者割合',
    startangle=90,
    counterclock=False
)
plt.savefig('images/survived_pd_pie.png')
plt.show()

survived_series.plot(
    kind='bar',
    title='生存人数と死亡人数',
    rot=0
)
plt.savefig('images/survived_pd_bar.png')
plt.show()


# matplotlib
# (辞書使用)
survived_dict = {'生存者数': survived, '死亡者数': died}
print(survived_dict.keys(), survived_dict.values())
plt.title('生存者割合')
plt.pie(
    x=survived_dict.values(),
    labels=survived_dict.keys(),
    counterclock=False,
    shadow=True,
    startangle=90,
    autopct='%1.1f%%',
    explode=[0.1, 0]
)
plt.savefig('images/survived_plt_pie.png')
plt.show()

plt.title('生存人数と死亡人数')
plt.bar(
    x=survived_dict.keys(),
    height=survived_dict.values(),
    align='center'
)
plt.ylabel('人数（人）')
plt.savefig('images/survived_plt_bar.png')
plt.show()

plt.title('生存者割合')
plt.pie(
    x=survived_dict.values(),
    labels=survived_dict.keys(),
    counterclock=False,
    shadow=True,
    startangle=90,
    autopct='%1.1f%%',
    explode=[0.1, 0]
)
plt.savefig('images/survived_plt_pie.png')
plt.show()

# ２つのグラフを横に並べて表示(辞書不使用)
plt.figure(figsize=(10, 4))

plt.subplot(121)
plt.title('生存人数と死亡人数')
plt.bar(
    x=['生存者数', '死亡者数'],
    height=[survived, died],
    align='center'
)
plt.ylabel('人数（人）')

plt.subplot(122)
plt.title('生存者割合')
plt.pie(
    x=[survived, died],
    labels=['生存者数', '死亡者数'],
    counterclock=False,
    shadow=True,
    startangle=90,
    autopct='%1.1f%%',
    explode=[0.1, 0]
)

plt.suptitle('Survived', fontsize=16)
plt.subplots_adjust(top=0.8)
plt.savefig('images/survived_plt.png')
plt.show()


# seaborn
pprint(sns.get_dataset_names())
'''
['anagrams',
 'anscombe',
 'attention',
 'brain_networks',
 'car_crashes',
 'diamonds',
 'dots',
 'exercise',
 'flights',
 'fmri',
 'gammas',
 'geyser',
 'iris',
 'mpg',
 'penguins',
 'planets',
 'tips',
 'titanic']
'''
# data = sns.load_dataset('titanic')
# print(data)
bar_graph = sns.countplot(x='Survived', data=train_df)
bar_graph.set_xticklabels(['生存者数', '死亡者数'])
bar_graph.get_figure().savefig('images/survived_sns_bar.png')
plt.show()
