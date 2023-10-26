from utils import input_num


def question_2():
    num = int(input_num('Which multiplication table would you like to print? '))
    size = int(input_num('How high would you like it to go? '))

    current = 1

    print('Here is your multiplication table:')
    while current <= size:
        print(f'{num} times {current} = {num * current}')
        current += 1
