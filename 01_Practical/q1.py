from utils import input_num

def question_1():
    # Define list which will store all the scores that the user inputs
    scores = []

    # Loop to input a score 5 times
    for i in range(5):
        scores.append(input_num(f'{[i+1]} Enter a score: '))

    # Calculate the average score and store it in the variable
    average_score = sum(scores) / len(scores)

    print(f'Average Score: {average_score}')
