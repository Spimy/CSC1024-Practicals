from utils import input_num

def question_4():
  # Constant for pricing
  PRICE_10GB = 15.00
  PRICE_EXCESS = 30.00

  data_usage_gb = input_num('Enter your monthly data usage in GB: ')

  if data_usage_gb <= 10:
    data_charges = data_usage_gb * PRICE_10GB

  else:
    '''
    The first 10GB is always going to be RM15.00
    This means that the data charges for the excess can be calulated by excluding the first 10GB
    The data charge for the first 10GB can then be calculated by simply adding its fixed price
    '''
    data_charges = ((data_usage_gb - 10) * PRICE_EXCESS) + (PRICE_10GB * 10)

  print(f'The cost of {data_usage_gb}GB data usage is: RM{data_charges}')
