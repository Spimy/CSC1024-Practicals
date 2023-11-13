from utils import input_num
from random import randint


def question_4():
    score = 0

    for i in range(5):
        num1 = randint(1, 1000)
        num2 = randint(1, 1000)
        ans = int(input_num(f'What is {num1} + {num2}?: '))

        if ans == num1 + num2:
            score += 1

    print(f'Your total score is: {score}')
