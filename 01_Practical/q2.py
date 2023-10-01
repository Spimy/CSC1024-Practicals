from utils import input_num

def question_2():
  # Exchange rate from rm to sgd
  exchange_rate = 3.04

  # User inputs amount in rm
  amount_rm = input_num('Enter your amount in RM: ')

  # Calculate amount in sgd and round to 2 decimal places
  amount_sgd = round(amount_rm / exchange_rate, 2)

  print(f'RM{amount_rm} -> {amount_sgd}SGD')
