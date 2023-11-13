from sys import maxsize
from utils import input_num


def question_6():
    print('A program to find the maximum and minimum numbers in a list.')
    print('Enter ten (10) numbers into a list.')

    my_list = []
    for i in range(10):
        my_list.append(input_num('Enter a number: '))

    min_num = maxsize
    max_num = -maxsize - 1

    for i in range(len(my_list)):
        if my_list[i] < min_num:
            min_num = my_list[i]

        if my_list[i] > max_num:
            max_num = my_list[i]

    print(f'Maximum Number: {max_num}')
    print(f'Minimum Number: {min_num}')
