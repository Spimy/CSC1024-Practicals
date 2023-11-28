from utils import input_num
from random import randint


def question_2():
    num = int(input_num('Display multiplication table of? '))
    table = [f'{num} x {i+1:>2} = {num * (i+1):>2}' for i in range(12)]

    with open('TT2TXT.txt', 'w') as file:
        file.write('\n'.join(table))

    print(f'A multiplication table of {num} times 1 to 12.')
    with open('TT2TXT.txt', 'r') as file:
        print(file.read())
