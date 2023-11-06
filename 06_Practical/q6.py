def question_6():
    i = 0
    my_list = []

    while i < 5:
        num = input('Enter a data: ')
        my_list.append(num)
        i += 1

    while i >= 0:
        if i % 2 == 0:
            print(my_list)
            del my_list[i]
        i -= 1

    print(my_list)
