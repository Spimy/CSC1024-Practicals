from utils import input_num


def question_6():
    characters = 'abcdefghijklmnopqrstuvwxyz'

    while True:
        selection = ''

        while selection not in ('encode', 'decode'):
            selection = input(
                "Type 'encode' to encrypt, type 'decode' to decrypt: ")

        msg = input('Type your message: ')
        shift = int(input_num('Type the shift number: '))

        i = 0
        result = ''

        while i < len(msg):
            try:
                if selection == 'decode':
                    new_index = (characters.index(msg[i]) - shift) % len(characters)
                else:
                    new_index = (characters.index(msg[i]) + shift) % len(characters)
                result += characters[new_index]
            except ValueError:
                result += msg[i]

            i += 1

        print(f'The {selection}d text is {result}')

        cont = ''

        while cont.lower() not in ('yes', 'no'):
            cont = input(
                "Type 'yes' if you want to go again. Otherwise, type 'no': "
            )

        if cont.lower() == 'no':
            break
        else:
            # Print a new line before restarting
            print()
