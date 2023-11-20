from sys import maxsize
from utils import input_num


def question_4():
    print('A program to find the maximum and minimum numbers in a list.')
    amount = int(
        input_num('Enter how many numbers you want to read into a list: '))

    user_list = read_number(amount)

    max_num = find_max_number(user_list)
    min_num = find_min_number(user_list)

    print(f'Maximum Number: {max_num}')
    print(f'Minimum Number: {min_num}')


def read_number(total_number_to_read):
    user_list = []

    for i in range(total_number_to_read):
        user_list.append(input_num('Enter a number: '))

    return user_list


def find_max_number(a_list_of_num):
    max_num = -maxsize - 1

    for i in range(len(a_list_of_num)):
        if a_list_of_num[i] > max_num:
            max_num = a_list_of_num[i]

    return max_num


def find_min_number(a_list_of_num):
    min_num = maxsize

    for i in range(len(a_list_of_num)):
        if a_list_of_num[i] < min_num:
            min_num = a_list_of_num[i]

    return min_num
