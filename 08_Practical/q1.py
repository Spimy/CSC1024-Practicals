from utils import input_num


def question_1():
    num = int(input_num('Enter a number: '))
    count_num(num)


def count_num(num):
    print('\n'.join([str(i) for i in range(1, num + 1)]))
