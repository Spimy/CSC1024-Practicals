from utils import input_num
from q1 import question_1
from q2 import question_2
from q3 import question_3
from q4 import question_4
from q5 import question_5
from q6 import question_6

def main():
  question_num = int(input_num('Enter a question number: '))

  match(question_num):
    case 1: question_1() 
    case 2: question_2()
    case 3: question_3()
    case 4: question_4()
    case 5: question_5()
    case 6: question_6()
    case _: main()

if __name__ == '__main__':
  main()