# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 13:54:58 2022

@author: Computer Science ~ B
"""

def find_values(tuple_list):
    '''Returns tuple w/ sums of 1st num, 2nd num, and all nums'''
    sum1 = 0
    sum2 = 0
    sum_all = 0
    for numbers in tuple_list:
        num1 = numbers[0]
        num2 = numbers[1]
        sum1 += num1
        sum2 += num2
        sum_all += num1 + num2
    return (sum1, sum2, sum_all)

def write_sums(sums):
    return f'{sums[0]}  {sums[1]}  {sums[2]}'

sums = find_values([(3, 4), (1, 2), (9, -10), (55, 0)])
print(write_sums(sums))