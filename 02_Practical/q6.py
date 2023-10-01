from utils import input_num


def question_6():
  week_day = int(input_num('Enter day of the week: '))
  output_string = 'Drink of the day:'

  match (week_day):
    case 1: print(f'{output_string} Peppermint Mocha')
    case 2: print(f'{output_string} Candy Bar Latte')
    case 3: print(f'{output_string} Caramel Coffee')
    case 4: print(f'{output_string} Chocolate Almond Cafe Au Lait')
    case 5: print(f'{output_string} Pumpkin-Chai Latte')
    case 6: print(f'{output_string} Vanilla Chai Tea')
    case 7: print(f'{output_string} Gingerbread Latte')
    case _: question_6() # Recursively call this function until a valid input 