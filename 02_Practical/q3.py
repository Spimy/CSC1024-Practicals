from utils import input_num


def question_3():
    yearly_income = input_num('Enter your yearly income: ')

    # Set the tax rate based on yearly income
    if yearly_income <= 2_500:
        tax_rate = 0

    elif 2_501 <= yearly_income <= 10_000:
        tax_rate = 0.05

    elif 10_001 <= yearly_income <= 50_000:
        tax_rate = 0.15

    else:
        tax_rate = 0.25

    # Calculate total tax once only so it is easier to refactor code
    total_tax = yearly_income * tax_rate
    print(f'Total tax: RM{total_tax:.2f}')
