from utils import input_num

def question_5():
  mass = input_num('Enter mass of object in kg: ')
  velocity = input_num('Enter velocity of object in ms-1: ')

  # Calculate momentum of object
  momentum = mass * velocity

  # Calculate kinetic energy of object
  kinetic_energy = 0.5 * mass * (velocity ** 2)

  print(f'Momentum of object: {momentum}kgms-1')
  print(f'Kinetic energy of object: {kinetic_energy}J')
