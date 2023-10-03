'''
num room at least 10: 10% discount
num room at least 20: 20% discount
num room at least 30: 30% discount
at least 3 days: additional 5% discount

Input:
  - cost of renting 1 room
  - num rooms booked
  - num days booked
  - sales tax (%)

Output:
  - cost of renting 1 room including discount
  - discount on each room as percentage
  - num rooms booked
  - num days booked
  - total cost of rooms
  - sales tax
  - total billing (include sales tax)
'''

from utils import input_num


def question_10():
    # Constants
    DISCOUNT_3_DAYS = 0.05

    # Prompt user to enter necessary information
    cost_one_room = input_num('Enter cost of renting 1 room: ')
    num_rooms = int(input_num('Number of rooms: '))
    num_days = int(input_num('Number of days: '))
    sales_tax = input_num('Sales tax as percentage: ')

    # Set discount
    discount = 0

    if num_rooms >= 10:
        discount = 0.1

    elif num_rooms >= 20:
        discount = 0.2

    elif num_rooms >= 30:
        discount = 0.3

    # Calculate percentage discount of 1 room
    cost_discounted_room = (1.0 - discount) * (cost_one_room * num_days)

    # Calculate total cost without tax
    total_cost = cost_discounted_room * num_rooms

    if num_days >= 3:
        total_cost *= (1 - DISCOUNT_3_DAYS)

    print(f'Cost of 1 room: ${cost_discounted_room}')
    print(f'Discount percentage: {discount * 100}%')
    print(f'Total cost: ${total_cost}')
    print(f'Total bill inc. tax: ${total_cost * (1 + (sales_tax / 100))}')
