from q1 import question_1


def question_2():
    # Look... I didn't want to repeat code so I've gone ahead used what was returned in q1
    my_list = question_1()
    total = sum(my_list)

    print(f'Sum: {total}')
    print(f'Average: {total / len(my_list)}')
