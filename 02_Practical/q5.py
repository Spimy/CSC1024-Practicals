from utils import input_num

def question_5():
  '''
  Ask user whether they want to calculate area of rectangle or circle
  R / r: rectangle
  C / c: circle
  If neither of the allowed inputs are provided, call this function recursively until a valid input
  '''
  choice = input('Enter R(r) for rectangle or C(c) for circle area calculation: ')

  match (choice.lower()):
    case 'r': print(f'Area of rectangle: {area_rectangle()}')
    case 'c': print(f'Area of circle: {area_circle()}')
    case _: question_5()

def area_rectangle():
  length = input_num('Enter length of rectangle: ')
  width = input_num('Enter width of rectangle: ')
  return length * width

def area_circle():
  PI = 3.14159
  radius = input_num('Enter radius of circle: ')
  return PI * (radius ** 2)
