from utils import input_num


def question_6():
    a = int(input_num('Enter the first term (a): '))
    d = int(input_num('Enter the common difference (d): '))
    n = int(input_num('Enter the number of terms to be added (n): '))

    i = 0
    total = 0

    while i < n:
        total += a + i * d
        i += 1

    print('Sum of progression:', total)
