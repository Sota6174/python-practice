# 関数
def half_value(x):
    return x / 2


def f(x):
    if x % 2 == 0:
        return x
    else:
        return '2で割り切れない'


print("half_value(10): ", half_value(10))
print("f(10): ", f(10))
print()

# ラムダ式(無名関数とも呼ばれる): lanbda 引数: 返り値
print("lambda1: ", (lambda x: x / 2)(10))
print("lambda2: ", (lambda x: x if x % 2 == 0 else '2で割り切れない')(10))
print()

# ラムダ式 + 高層関数(引数に普通の関数ではなくラムダ式を渡す)
l_list = [i for i in range(10)]
print("l_list: ", l_list)

l2_list = list(map(lambda x: x**2, l_list))
print("l2_list: ", l2_list)
l2_list = [i**2 for i in range(10)]
print("l2_list: ", l2_list)
print()

# filter()メソッドは第1引数でTrueかFalseを返す関数を指定する必要がある
l3_list = list(filter(lambda x: x % 2 == 0, l_list))
print("l3_list: ", l3_list)
l3_list = [i for i in l_list if i % 2 == 0]
print("l3_list: ", l3_list)
print()

# 例外処理(エラーハンドリング)
# APIやスクレイピングなどのネットワークを介した処理を記述する際
# 画像ファイルやCVSファイルなどのファイルを開く処理を記述する際に有用


def divide_func1(a, b):
    try:
        sum = a / b
    except TypeError as e:
        print("catch TypeError: ", e)
        return 'TypeError'
    except ZeroDivisionError as e:
        print("catch ZeroDivisionError: ", e)
        return 'ZeroDivisionError'
    else:   # 成功時に実行される
        print("エラーなし")
        return sum
    finally:    # 常に最後に行われる処理
        print("例外処理終了")


def divide_func2(a, b):
    try:
        sum = a / b
    except (TypeError, ZeroDivisionError):
        pass    # 例外をキャッチしても特別な処理をせずにスルーしたい時はpass
    else:
        return sum


print(f"func1: 10 / 20 = {divide_func1(10, 20)}\n")
print(f"func1: 10 / '20' = {divide_func1(10, '20')}\n")
print(f"func1: 10 / 0 = {divide_func1(10, 0)}\n")

print(f"func2: 10 / 5 = {divide_func2(10, 5)}\n")
print(f"func2: 10 / 0 = {divide_func2(10, 0)}\n")
