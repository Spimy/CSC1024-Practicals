from utils import input_num

def question_4():
  length = input_num('Enter length of rectangle: ')
  height = input_num('Enter height of rectangle: ')

  # Calculate area of rectangle from length and height
  area = length * height

  # Calculate perimeter of rectangle from length and height
  perimeter = 2 * (length + height)

  print(f'Area of rectangle: {area}')
  print(f'Perimeter of rectangle: {perimeter}')
