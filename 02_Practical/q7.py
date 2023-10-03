'''
box -> 24 cookies
container -> 75 boxes
=> 1 container -> 24 * 75 cookies

input num cookies
output: num boxes and num containers for the num cookies

if last box contains less than 24 cookies, then discard
=> also output num left over cookies

if last container contains less than 75 boxes, then discard
=> also output num left over boxes
'''

from utils import input_num


def question_7():
    # Constants
    COOKIES_PER_BOX = 24
    BOXES_PER_CONTAINER = 75

    # Prompt user to enter number of cookies
    num_cookies = int(input_num('Enter number of cookies: '))

    # Calculate number of boxes to fit the cookies into and the remaining cookies that could not fit into a box
    num_boxes = num_cookies // COOKIES_PER_BOX
    num_cookies_left = num_cookies % COOKIES_PER_BOX

    # Calculate number of containers to fit the boxes into and the remaining boxes that could not fit into a container
    num_containers = num_boxes // BOXES_PER_CONTAINER
    num_boxes_left = num_boxes % BOXES_PER_CONTAINER

    print()  # For extra new line in terminal

    print(f'Number of boxes for cookies: {num_boxes}')
    print(f'Number of containers for boxes of cookies: {num_containers}')

    print()  # For extra new line in terminal

    if num_cookies_left > 0:
        print(
            f'Number of leftover cookies that could not fit into a box of 24: {num_cookies_left}'
        )

    if num_boxes_left > 0:
        print(
            f'Number of leftover boxes that could not fit into a container of 75: {num_boxes_left}'
        )
