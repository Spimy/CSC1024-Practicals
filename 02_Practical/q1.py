from utils import input_num

def question_1():
  # Constants for price of new and old videos
  NEW_VID_PRICE = 3
  OLD_VID_PRICE = 2
  
  # Prompt user to input information about rentind new videos
  num_new = int(input_num('Enter number of new videos to rent: '))
  num_days_rented_new = int(input_num('Enter number of days to rent videos: '))

  # Prompt user to input information about rentind old videos
  num_old = int(input_num('Enter number of old videos to rent: '))
  num_days_rented_old = int(input_num('Enter number of days to rent videos: '))

  cost_new_vid = num_new * num_days_rented_new * NEW_VID_PRICE
  cost_old_vid = num_old * num_days_rented_old * OLD_VID_PRICE

  total_cost = cost_new_vid + cost_old_vid
  print(f'Total cost of video rental: ${total_cost}')

