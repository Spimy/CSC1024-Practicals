from utils import input_num


def question_8():
    square_size = 0

    while square_size < 1 or square_size > 20:
        square_size = int(input_num('Enter size of square: '))

    row = 0
    while row < square_size:
        column = 0

        while column < square_size:
            if 0 < row < square_size - 1 and 0 < column < square_size - 1:
                print(' ', end=' ')
            else:
                print('*', end=' ')
            column += 1

        row += 1
        print()
