from q1 import question_1


def question_3():
    # Again... I didn't want to repeat code so I've gone ahead used what was returned in q1
    forward_list = question_1()
    print('Forward list: ', forward_list)

    # Ok fine I did not read that it said do not use built-in functions except append and sort
    # print('Reverse list: ', list(reversed(forward_list)))

    # Just following the rules :)
    forward_list.sort(reverse=True)
    print('Reverse list: ', forward_list)
