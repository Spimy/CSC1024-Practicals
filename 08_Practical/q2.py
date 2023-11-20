from utils import input_num
from random import randint


def question_2():
    num1 = int(input_num('Enter first number: '))
    num2 = None

    while num2 is None or num2 < num1:
        num2 = int(input_num('Enter second number: '))

    comp_num = randint(num1, num2)

    print_thought()

    guess = None
    checker = {
        'correct': False,
        'message': ''
    }

    while guess is None or not checker['correct']:
        guess = int(input_num('Enter your guess: '))
        checker = check_answer(guess, comp_num)
        print(f'[{checker["message"]}]', end=' ')

    print()


def print_thought():
    print('I am thinking of a number... Can you guess it?')


def check_answer(answer, comp_num):
    if answer < comp_num:
        return {
            'correct': False,
            'message': 'Guess was too low'
        }

    if answer > comp_num:
        return {
            'correct': False,
            'message': 'Guess was too high'
        }

    return {
        'correct': True,
        'message': 'Correct, you win'
    }
