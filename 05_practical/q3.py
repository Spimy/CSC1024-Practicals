def question_3():
    i = 0

    while i < 5:

        j = 0
        while j < 11:
            if j % 2 == 0:
                print(1, end='')
            else:
                print(0, end='')
            j += 1

        print()
        i += 1
