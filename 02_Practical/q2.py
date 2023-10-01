from utils import input_num

def question_2():
  time_elapsed_seconds = int(input_num('Enter number of seconds lapsed for event: '))

  hours = time_elapsed_seconds // 3600
  minutes = (time_elapsed_seconds % 3600) // 60
  time_elapsed_seconds %= 3600 // 60

  print(f'{hours}:{minutes}:{time_elapsed_seconds}')
