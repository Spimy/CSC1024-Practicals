from utils import input_num


def question_1():
    i = 0
    my_list = []

    while i < 5:
        num = input_num('Enter a number: ')
        my_list.append(num)
        i += 1

    my_list.sort()
    print(my_list)

    return my_list
