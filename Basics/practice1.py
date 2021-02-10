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

# リスト
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
'''
l_list = []
for i in range(5):
    l_list.append(i*2)
より高速
'''
l_list = [i*2 for i in range(5)]
print("[i*2 for i in range(5)]: ", l_list)
print()

l_list = [i for i in range(10) if i % 2 == 0]
print("[i for i in range(10) if i % 2 == 0]: ", l_list)
print()

# 処理時間
# google colaboratory, jupyter notebookはマジックコマンド(%%timeit)が使える
