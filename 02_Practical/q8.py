from utils import input_num


def input_operator(display_text):
    OPERATOR_LIST = ['+', '-', '*', '/']
    operator = ''

    while operator not in OPERATOR_LIST:
        operator = input(display_text)

    return operator


def question_8():
    # Prompt user to enter the numbers and operator
    num_x = input_num('Enter the first number: ')
    operator = input_operator('Enter the operator: ')
    num_y = input_num('Enter the second number: ')

    # Form the expression for the output string
    expression = f'{num_x} {operator} {num_y}'

    # Do the math operations based on the operator provided
    match (operator):
        case '+': print(f'{expression} = {num_x + num_y}')
        case '-': print(f'{expression} = {num_x - num_y}')
        case '*': print(f'{expression} = {num_x * num_y}')
        # Use ternary operator to output the appropriate string
        case '/': print(f'{expression} = {num_x / num_y}') if num_y != 0 else print(f'{expression} cannot devide by zero')
