import random

from termcolor import colored

word_dict = {
    'AFAIK(AS Far As I know)': '自分が知っている限りでは',
    'FYI(For Your Information)': 'ご参考までに',
    'GOTCHA(I\'ve Got You)': 'やった！',
    'IMO(In My Opinion)': '個人的には',
    'LGTM(Looks Good To Me)': '自分的にはOK！',
    'TBD(To Be Determined)': 'あとで決める',
}

# template = '*' * 15 + '\n英単語: {}\n日本語: \n' + '*' * 15

while(1):
    # 英単語を表示する
    word = random.choice(list(word_dict.keys()))

    # 日本語を入力する
    # print(template.format(word))
    answer = input(word+': ')

    # 答えとあっているか確認する
    if len(answer) == 0:
        break
    if answer == word_dict[word]:
        print(colored("正解!!\n", color='green'))
    else:
        print(colored("不正解", color='red'))
        print(f"{word}: {word_dict[word]}\n")
