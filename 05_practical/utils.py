def input_num(display_text):
    '''
    Ask user to input a number
    If the input was not a number, recurse the function until it is a number
    '''

    try:
        return float(input(display_text))
    except:
        return input_num(display_text)
