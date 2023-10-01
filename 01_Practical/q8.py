from utils import input_num

def question_8():
    hourly_wage = input_num('Enter hourly wage: ')
    total_reg_hours = input_num('Enter total regular hours: ')
    total_overtime_hours = input_num('Enter total overtime hours: ')

    weekly_wage = hourly_wage * total_reg_hours + \
        1.5 * hourly_wage * total_overtime_hours

    print(f'Total weekly pay of an employee: RM{weekly_wage}')
