'''
Option 1:
$5000 -> final manuscript
$20,000 -> novel published

Option 2:
12.5% net price of each copy sold

Option 3:
10% net price of first 4000 copies sold
14% net price of > 4000 copies sold

Input: net price & estimate number of copies sold
Output: royalties for each option & best option
'''

from utils import input_num


def question_9():
    # Constants
    BREAKPOINT = 4000
    PERCENTAGE_OPT_2 = 0.125
    PERCENTAGE_OPT_3_LBREAKPOINT = 0.10  # Less than BREAKPOINT
    PERCENTAGE_OPT_3_MBREAKPOINT = 0.14  # More than BREAKPOINT

    # Prompt user the enter the necessary information
    net_price = input_num('Enter net price: ')
    estimated_sales = int(input_num('Enter estimate number of sales: '))

    # Option 1
    total_opt_1 = 5000 + 20_000

    # Option 2
    total_opt_2 = (net_price * PERCENTAGE_OPT_2) * estimated_sales

    # Option 3
    if estimated_sales <= BREAKPOINT:
        total_opt_3 = (net_price * PERCENTAGE_OPT_3_LBREAKPOINT) * \
            estimated_sales
    else:
        remaining_sales = estimated_sales - BREAKPOINT
        total_opt_3 = \
            ((net_price * PERCENTAGE_OPT_3_MBREAKPOINT) * remaining_sales) + \
            ((net_price * PERCENTAGE_OPT_3_LBREAKPOINT) * BREAKPOINT)

    # Select best option
    best_option = 1

    if total_opt_1 < total_opt_2:
        best_option = 2

    if total_opt_2 < total_opt_3:
        best_option = 3

    print(f'Royalties for Option 1: ${total_opt_1:,.2f}')
    print(f'Royalties for Option 2: ${total_opt_2:,.2f}')
    print(f'Royalties for Option 3: ${total_opt_3:,.2f}')
    print(f'Best option: Option {best_option}')
