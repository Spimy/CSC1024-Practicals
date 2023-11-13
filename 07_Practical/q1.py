from utils import input_num


def question_1():
    num = int(input_num('Enter a number (1-12): '))

    # Ayo question asked for it... I didn't want recursion but no while loops allowed
    if num < 1 or num > 12:
        return question_1()

    for i in range(10):
        print(f'{i + 1} x {num} = {(i + 1) * num}')
