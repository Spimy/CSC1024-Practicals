# d = 0.5g(t^2)
def question_7():
    time = 10  # in seconds
    acceleration = 32  # in ft/sec^2

    i = 0
    cumulative_distance = 0

    print(f'{"Time":<9} {"Interval Distance"} {"Total Distance":>20}')
    while i <= time:
        interval_distance = 0.5 * acceleration * (i ** 2)
        cumulative_distance += interval_distance

        print(f'{i:<20} {interval_distance:>6} {cumulative_distance:>20}')
        i += 1
