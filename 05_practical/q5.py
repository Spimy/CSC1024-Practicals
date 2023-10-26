from utils import input_num


def question_5():
    p = input_num('Enter the initial principal: RM')
    r = input_num('Enter the interest rate: ')
    n = int(input_num('Enter the number of years: '))

    print('\n' * 2)

    print('Compound Interest Calculation')
    print('Initial Principal: RM', p)
    print('Interest Rate: ', r)
    print('Number of Years: ', n)

    print()

    col_name = 'Total amount on deposit (RM)'
    print(f'{"Year":<10} {col_name}',)

    current_year = 1
    while current_year <= n:
        cur = str(current_year).rjust(len(str(n)), ' ')
        a = f'{(p * (1 + r) ** current_year):.2f}'

        print(
            f'{cur:>{2 + len(cur)}} {a:>{len(str(a)) + len(col_name) - 1}}'
        )

        current_year += 1
