from math import pi
from utils import input_num

def question_6():
  radius = input_num('Enter radius of sphere: ')

  # Calculate the diameter of the sphere
  diameter = radius * 2

  # Calculate the circumference of the sphere and round to 2 decimal places
  circumference = round(2 * pi * radius, 2)

  # Calculate the surface area of the sphere and round to 2 decimal places
  surface_area = round(4 * pi * (radius ** 2), 2)

  # Calculate the volume of the sphere and round to 2 decimal places
  volume = round((4 / 3) * pi * (radius ** 3), 2)

  print(f'Diameter of sphere: {diameter}')
  print(f'Circumference of sphere: {circumference}')
  print(f'Surface area of sphere: {surface_area}')
  print(f'Volume of sphere: {volume}')
