import timeit

# 演算
a = 5
b = 3
print(f"{a} / {b}の商: {a} // {b} = {a // b}")
print(f"{a} / {b}の余り: {a} % {b} = {a % b}")
print(f"{a}の{b}乗: {a} ** {b} = {a ** b}\n")


# 文字列
s_str = "文字列の練習"
print(s_str)    # 文字列の練習
print(f"s_str[0]: {s_str[0]}, s_str[3]: {s_str[3]}, s_str[-1]: {s_str[-1]}\n")

s_str = "スライスの練習"
print(s_str)        # 文字列の練習
print(s_str[:])     # スライスの練習
print(s_str[:4])    # スライス
print(s_str[1:4])   # ライス
print(s_str[5:])    # 練習
print()

# キャスト
print(str(a) + str(b))
print(f"a == 5: {a == 5}")
print(f"a == str(a): {a == str(a)}\n")

# for文
s_str = "for文の練習"
for i in range(len(s_str)):
    print(s_str[i])
print()

for i in s_str:
    print(i)
print()

for i in range(1, 10, 2):   # start=1, stop=10, step=2
    if i == 3:
        continue
    print("i = ", i)
print()

# while文
i = 0
while i < 100:
    i += 1  # i++は使えない
print("i = ", i)

i = 0
while(1):
    i += 1
    if i >= 100:
        break
print("i = ", i)

# [リスト]
l_list = [0, 2, 4, 6, 8, 10]
print("l_list: ", l_list)
print(type(l_list))
print()

for i, item in enumerate(l_list):
    print(f"l_list[{i}] = {item}")
print()

l_list.append(10)
print(l_list)
print()

l_list.insert(2, 3)
print(l_list)
print()

l_list.remove(10)   # 1つ目だけ削除
print(l_list)
print()

# 内包表記
l_list = [i*2 for i in range(5)]
print("[i*2 for i in range(5)]: ", l_list)
print()

l_list = [i for i in range(10) if i % 2 == 0]
print("[i for i in range(10) if i % 2 == 0]: ", l_list)
print()

# 処理時間
# google colaboratory, jupyter notebookはマジックコマンド(%%timeit)が使える


def func1():
    l_list = []
    for i in range(100):
        l_list.append(i)


def func2():
    l_list = [i for i in range(100)]


processing_time = timeit.timeit(stmt=func1, number=100)
print(f"processing_time: {processing_time/100:.7f}[sec]\n")

processing_time = timeit.timeit(stmt=func2, number=100)
print(f"processing_time: {processing_time/100:.7f}[sec]\n")

# (タプル)：変更されたくない値の保管などで有効
t_tuple = (0, 1, 2)     # リストと違って内容が変更出来ない

t1_tuple = (0, 1)
t2_tuple = (2, 3)
print(f"t1_tuple: {t1_tuple}, type: {type(t1_tuple)}, id: {id(t1_tuple)}")
print(f"t2_tuple: {t2_tuple}, type: {type(t2_tuple)}, id: {id(t2_tuple)}")

t1_tuple = t1_tuple + t2_tuple  # 新しいt1_tupleが作成されるt1_tuple = (0, 1, 2, 3)と同じ
print(f"t1_tuple: {t1_tuple}, type: {type(t1_tuple)}, id: {id(t1_tuple)}")

# {辞書}
d_dict = {'a': 1, 'b': 20, 'c': 30}
print(f"d_dict: {d_dict}, type: {type(d_dict)}")
d_dict['a'] = 10
d_dict['d'] = 40
print(f"d_dict: {d_dict}")
print(f"d_dict.keys: {d_dict.keys()}")
print(f"d_dict.values: {d_dict.values()}")
print(f"d_dict.items: {d_dict.items()}")

for key, value in d_dict.items():
    print(f"key: {key}, value: {value}")

# 辞書: get()メソッドは値がない時、Noneを返し、keyerrorにならない
print("\ndict.get()")
print(f"d_dict.get('a'): {d_dict.get('a')}")
print(f"d_dict.get('e'): {d_dict.get('e')}")
print(f"d_dict: {d_dict}")

# 辞書: pop()メソッドは辞書から値を取り出す
print("\ndict.pop()")
print(f"d_dict.pop('a'): {d_dict.pop('a')}")
print(f"d_dict: {d_dict}\n")

# {集合}: 重複は1つに、順序は順番になる
s_set = {1, 1, 2, 9, 8, 4, 5}
print(f"s_set: {s_set}, type: {type(s_set)}")
s_set = {'a', 'a', 'd', 'c', 'b', 'b', 'b'}
print(f"s_set: {s_set}, type: {type(s_set)}")

a_set = {0, 1, 2, 3, 4, 5, 6}
b_set = {0, 2, 4, 6, 8}
print('a_set: ', a_set)
print('b_set: ', b_set)
print('差集合(a - b): \t', a_set - b_set)
print('差集合(b - a): \t', b_set - a_set)
print('積集合(a かつ b): \t', a_set & b_set)
print('和集合(a または b): \t', a_set | b_set)
print('排他的論理和(a ^ b = (a または b) - (a かつ b)): ', a_set ^ b_set)
