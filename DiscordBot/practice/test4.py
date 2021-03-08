FLOOR_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '20', '25', '27', '35', '37', '40', '47']
number_tofull = dict((0x0030 + ch, 0xFF10 + ch) for ch in range(10))


def num_translate(x: int):
    return x.translate(number_tofull)


print(number_tofull)
print(list(map(num_translate, FLOOR_list)))
