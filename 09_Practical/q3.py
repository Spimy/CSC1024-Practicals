from utils import input_num
from random import randint


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def from_string(str):
        return Employee(*str.split(', '))

    def __str__(self):
        return f'{self.name}, {self.age}'



def question_3():
    employees = []

    with open('employee.txt', 'r') as file:
        employees = list(
            map(lambda x: Employee.from_string(x), file.read().splitlines())
        )

    while True:
        name = input('Enter name (or DONE to quit): ')

        if name.upper() == 'DONE':
            break

        age = int(input_num('Enter age: '))
        employees.append(Employee(name, age))

    employees.sort(key=lambda x: x.name)
    employees = ['Employee Name, Age'] + list(map(lambda x: str(x), employees))

    with open('updated_employee.txt', 'w+') as file:
        file.write('\n'.join(employees))
