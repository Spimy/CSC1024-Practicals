from utils import input_num
import math


def question_4():
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

        while lower_range <= upper_range:
            if selection == 1:
                print(f'{lower_range}C = {((lower_range * 9/5) + 32):.2f}F')
            else:
                print(f'{lower_range}F = {((lower_range - 32) * 5/9):.2f}C')

            lower_range += 1
        print('Conversion Done!')

        cont = ''
        while cont.upper() not in ('Y', 'N'):
            cont = input('Do you want to run the program again? [Y/N]: ')

        if cont.upper() == 'N':
            break
        else:
            # Add new line before restarting
            print()


def range_input():
    lower_range = None
    upper_range = None

    # Second condition tests if input is integer or float
    # If flooring it gives the same result as itself, then it must be an integer
    while lower_range is None or math.floor(lower_range) != lower_range:
        lower_range = input_num('Enter minimum temperature: ')

    while upper_range is None or math.floor(upper_range) != upper_range:
        upper_range = input_num('Enter maximum temperature: ')

    return (int(lower_range), int(upper_range))
