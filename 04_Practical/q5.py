from utils import input_num


def question_5():
    secret_num = 50

    guess = 0
    num_attempts = 0

    while guess != secret_num:
        guess = int(input_num('Guess the secret number: '))

        if guess < secret_num:
            print('Your guess was too low.')

        if guess > secret_num:
            print('Your guess was too high.')

        num_attempts += 1

    print(f'Well done, you took {num_attempts} attempts')
