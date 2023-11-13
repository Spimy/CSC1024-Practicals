from utils import input_num
import math


def question_5():
    while True:
        print('Temperature Conversion Programme.')
        print('[1] Convert Celsius to Fahrenheit.')
        print('[2] Convert Fahrenheit to Celsius')

        selection = int(input_num('Enter your selection, 1 or 2: '))

        if selection == 1:
            print('Celsius (C) to Fahrenheit (F) Conversion')
        elif selection == 2:
            print('Fahrenheit (F) to Celsius (C) Conversion')
        else:
            print('ERROR: Invalid Selection!')
            # Add new line before restarting
            print()
            continue

        lower_range, upper_range = range_input()

        for current in range(lower_range, upper_range + 1):
            if selection == 1:
                print(f'{current}C = {((current * 9/5) + 32):.2f}F')
            else:
                print(f'{current}F = {((current - 32) * 5/9):.2f}C')
        print('Conversion Done!')

        cont = cont_input()
        if cont == 'Y':
            print()
        else:
            break


def range_input(lower_range=None, upper_range=None):
    if lower_range is None:
        lower_range = input_num('Enter minimum temperature: ')

    if lower_range is None or math.floor(lower_range) != lower_range:
        return range_input()

    if upper_range is None:
        upper_range = input_num('Enter maximum temperature: ')

    if upper_range is None or math.floor(upper_range) != upper_range:
        return range_input(lower_range)

    if upper_range < lower_range:
        return range_input()

    return (int(lower_range), int(upper_range))


def cont_input():
    cont = input('Do you want to run the program again? [Y/N]: ').upper()

    if cont not in ('Y', 'N'):
        return cont_input()

    return cont
