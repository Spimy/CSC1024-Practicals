from utils import input_num


def question_8():
    square_size = 0

    while square_size < 1 or square_size > 20:
        square_size = int(input_num('Enter size of square: '))

    i = 0
    while i < square_size:
        j = 0

        while j < square_size:
            if 0 < i < square_size - 1 and 0 < j < square_size - 1:
                print(' ', end=' ')
            else:
                print('*', end=' ')
            j += 1

        i += 1
        print()
