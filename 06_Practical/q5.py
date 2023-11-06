def question_5():
    i = 0
    my_list = []

    while i < 5:
        num = input('Enter a data: ')
        my_list.append(num)
        i += 1

    while len(my_list) > 0:
        print(my_list)
        del my_list[len(my_list)-1]

    print(my_list)
