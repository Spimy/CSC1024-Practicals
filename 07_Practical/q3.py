from utils import input_num


def question_3(direction=None):
    if direction is None:
        direction = input('Enter count "up" or "down": ').lower()

    if direction not in ('up', 'down'):
        return question_3()

    if direction == 'up':
        num = int(input_num('Enter top number (more than 1): '))

        if num <= 1:
            return question_3(direction)

        for i in range(1, num + 1):
            print(i)

    elif direction == 'down':
        num = int(input_num('Enter bottom number (less than 20): '))

        if num >= 20:
            return question_3(direction)

        for i in range(20, num - 1, -1):
            print(i)
