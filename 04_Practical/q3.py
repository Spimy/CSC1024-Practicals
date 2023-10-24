from utils import input_num


def question_3():
    a = int(input_num('Enter first number (a): '))
    b = int(input_num('Enter second number (b): '))

    i = 0
    ans = a

    while i < b - 1:
        ans *= a
        i += 1

    print('a^b =', ans)
