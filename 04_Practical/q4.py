import random


def question_4():
    done = False
    total = 0

    while not done:
        total += random.randint(1, 100)

        # Assume done so set variable done to True
        done = True

        # Set variable done back to false if input was not 'DONE'
        while input('Enter DONE to exit or anything else to continue: ').upper() != 'DONE':
            done = False
            break

    print('Total =', total)
