from utils import input_num


def question_2():
    num = int(input_num('Enter a number below 50: '))

    if num >= 50:
        return question_2()

    for i in range(50, num - 1, -1):
        print(i)
