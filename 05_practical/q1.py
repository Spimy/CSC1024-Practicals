from utils import input_num
from random import randint


def question_1():
    LOWER_LIMIT = 1
    UPPER_LIMIT = 200

    secret_num = randint(LOWER_LIMIT, UPPER_LIMIT)
    guess = 0
    num_attempts = 0

    while guess != secret_num:
        guess = int(input_num('Guess the secret number: '))

        if guess < secret_num:
            print('Your guess was too low.')
        elif guess > secret_num:
            print('Your guess was too high.')
        else:
            print(f'Well done, you took {num_attempts} attempts')

            # Ask if player wants to continue
            cont = ''

            while cont.lower() not in ('y', 'n'):
                cont = input('Do you want to play again? (y/n): ')

            if cont.lower() == 'y':
                secret_num = randint(LOWER_LIMIT, UPPER_LIMIT)
                guess = 0
                num_attempts = 0

                # Add new line before new game starts
                print()

        num_attempts += 1
