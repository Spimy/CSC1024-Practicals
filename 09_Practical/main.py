from utils import input_num
from q1 import question_1
from q2 import question_2
from q3 import question_3
from q4 import question_4


def main():
    question_num = int(input_num('Enter a question number: '))

    match(question_num):
        case 1: question_1()
        case 2: question_2()
        case 3: question_3()
        case 4: question_4()
        case _: main()


if __name__ == '__main__':
    main()
