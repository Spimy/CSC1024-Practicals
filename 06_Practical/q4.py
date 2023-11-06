from q1 import question_1


def question_4():
    # Again... I didn't want to repeat code so I've gone ahead used what was returned in q1
    my_list = question_1()

    while len(my_list) > 0:
        del my_list[len(my_list)-1]
        print(my_list)
