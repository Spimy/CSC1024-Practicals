from sys import maxsize
from utils import input_num


class Student:
    def __init__(self, name, t1, t2, t3):
        self.name = name
        self.t1 = float(t1)
        self.t2 = float(t2)
        self.t3 = float(t3)
        self.average = round((self.t1 + self.t2 + self.t3) / 3, 1)

    @staticmethod
    def from_string(str):
        return Student(*str.split(' '))

    def __str__(self):
        return f'{self.name} {self.t1} {self.t2} {self.t3} {self.average}'


def question_4():
    data = []

    with open('data.txt', 'r') as file:
        data = list(
            map(lambda x: Student.from_string(x), file.read().splitlines())
        )

    headers = ['Stu ID.', 'Test1', 'Test2', 'Test3', 'Average']
    prepared_data = [str(student).split(' ') for student in data]

    column_widths = [
        max(len(str(item)) for item in column) for column in zip(
            headers, *prepared_data
        )
    ]

    header_line = ' | '.join(
        f'{header:^{width}}' for header, width in zip(headers, column_widths)
    )

    with open('output.txt', 'w') as file:
        file.write(header_line + '\n')
        file.write(('-' * len(header_line)) + '\n')

        for row in prepared_data:
            row_line = " | ".join(
                f'{item:<{width}}' for item, width in zip(row, column_widths)
            )
            file.write(row_line + '\n')

        file.write('-' * len(header_line))
