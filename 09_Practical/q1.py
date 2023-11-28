from utils import input_num


def question_1():
    print('[1] Create a new file.')
    print('[2] Display the file.')
    print('[3] Add a new item to the file.')

    option = None

    while option is None or option not in (1, 2, 3):
        if option is not None:
            print('The only options allowed are 1, 2, or 3!')

        option = int(input_num('Enter 1, 2, or 3: '))

        match (option):
            case 1: create_file()
            case 2: display_file()
            case 3:
                add_subject()
                display_file()


def create_file():
    subject = input('Enter a subject: ')

    with open('Subject.txt', 'w+') as file:
        file.write(f'{subject}\n')


def display_file():
    with open('Subject.txt', 'r+') as file:
        print(file.read())


def add_subject():
    subject = input('Enter a subject: ')

    with open('Subject.txt', 'a+') as file:
        file.write(f'{subject}\n')
