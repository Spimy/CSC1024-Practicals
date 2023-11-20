from utils import input_num
from random import randint


def question_3():
    print('[1] Addition')
    print('[2] Subtraction')
    option = int(input_num('Enter 1 or 2: '))

    if option != 1 and option != 2:
        print('You can only select 1 or 2')
        return

    answers = {
        'user_ans': None,
        'correct_ans': None
    }

    if option == 1:
        answers = addition()
    else:
        answers = subtraction()

    if not is_correct(answers):
        print('Incorrect, the answer is: ', answers['correct_ans'])
        return

    print('Correct')


def addition():
    nums = [randint(5, 20) for i in range(2)]
    total = sum(nums)

    print('+'.join(str(i) for i in nums), end='')
    answer = int(input_num('= '))

    return {
        'user_ans': answer,
        'correct_ans': total
    }


def subtraction():
    nums = [randint(25, 50), -randint(1, 25)]
    difference = sum(nums)

    print(''.join(str(i) for i in nums), end='')
    answer = int(input_num('= '))

    return {
        'user_ans': answer,
        'correct_ans': difference
    }


def is_correct(answer):
    return answer['user_ans'] == answer['correct_ans']
