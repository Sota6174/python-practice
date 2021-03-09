import timeit
import random

FLOOR_list = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
    '11', '12', '13', '14', '20', '25', '27', '35', '37', '40', '47']
TASK_LIST = [
    '小瓶', '中瓶', 'mod開放の欠片Ⅱ・SS', '赤冥晶の欠片', '橙冥晶の欠片',
    '大瓶', 'mod開放の欠片Ⅲ', '黄冥晶の欠片', '緑冥晶の欠片',
    '武装石', 'コアメタル', '混沌の赤冥晶', '混沌の橙冥晶', '混沌の黄冥晶', '混沌の緑冥晶', '熟練度']
number_tofull = dict((0x0030 + ch, 0xFF10 + ch) for ch in range(10))


def num_translate(x: int):
    return x.translate(number_tofull)


def func1():
    quantity = random.randint(1, 10)
    if quantity > 5:
        task = TASK_LIST[random.randint(0, 4)]
    elif quantity > 1:
        task = TASK_LIST[random.randint(0, 8)]
    else:
        task = random.choice(TASK_LIST)


def func2():
    quantity = random.randint(1, 10)
    if quantity > 5:
        task = TASK_LIST[random.randint(0, 4)]
    elif quantity > 1:
        task = TASK_LIST[random.randint(0, 8)]
    else:
        task = TASK_LIST[random.randint(0, 15)]


def func3():
    quantity = random.randint(1, 10)
    if quantity > 5:
        task = random.choice(TASK_LIST[:5])
    elif quantity > 1:
        task = random.choice(TASK_LIST[:9])
    else:
        task = random.choice(TASK_LIST)


# for i in range(10):
#     print(random.randint(0, 4))
processing_time = timeit.timeit(stmt=func1, number=1000)
print(f"func1, 1000回：processing_time: {processing_time:.7f}[sec]\n")
# func1, 1000回：processing_time: 0.0016609[sec]
# func1, 1000回：processing_time: 0.0021984[sec]
# func1, 1000回：processing_time: 0.0016435[sec]

processing_time = timeit.timeit(stmt=func2, number=1000)
print(f"func2, 100回：processing_time: {processing_time:.7f}[sec]\n")
# func2, 1000回：processing_time: 0.0019828[sec]
# func2, 1000回：processing_time: 0.0018264[sec]
# func2, 1000回：processing_time: 0.0018264[sec]

processing_time = timeit.timeit(stmt=func3, number=1000)
print(f"func3, 1000回：processing_time: {processing_time:.7f}[sec]\n")
# func3, 1000回：processing_time: 0.0022833[sec]
# func3, 1000回：processing_time: 0.0014431[sec]
# func3, 1000回：processing_time: 0.0018054[sec]

# print(number_tofull)
# print(list(map(num_translate, FLOOR_list)))
