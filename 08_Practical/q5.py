from utils import input_num


def question_5():
    num = int(input_num('Enter a number: '))
    print('Reversed number:', reverse_int(num))


def reverse_int(num):
    reversed_num = 0

    while num != 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10

    return reversed_num
