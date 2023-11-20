from utils import input_num
from math import sqrt


def question_6():
    nums = [int(input_num('Enter a number: ')) for i in range(5)]

    print('Average:', calc_avg(nums))
    print('Standard Deviation:', calc_sd(nums))


def calc_avg(nums):
    return sum(nums) / len(nums)


def calc_sd(nums):
    avg = calc_avg(nums)
    return sqrt(sum(list(map(lambda x: (x - avg)**2, nums))) / len(nums))
