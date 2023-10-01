from utils import input_num

def question_7():
  bill_total = input_num('Enter the total bill amount: ')
  num_friends = int(input_num('Enter the number of friends: '))

  # Add 10% tax to the total bill amount
  bill_total *= 1.1

  # Add 6% GST to the total bill amount
  bill_total *= 1.06

  # Calculate amount to pay by each friend and round to 2 decimal places
  split_amount = round(bill_total / num_friends, 2)

  print(f'Amount to pay by each friend: RM{split_amount}')
