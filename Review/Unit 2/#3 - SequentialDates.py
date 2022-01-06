# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:10:58 2022

@author: Computer Science ~ B
"""

month = int(input('Enter the month as a number: '))
date = int(input('Enter the date: '))
year = int(input('Enter the year number: '))

yr_2dig = year % 100
dig_l = yr_2dig // 10
dig_r = yr_2dig % 10

if date == month + 1:
    if yr_2dig == date + 1:
        print(f'{month}/{date}/{yr_2dig} is sequential')
    elif dig_l == date + 1 and dig_r == dig_l + 1:
        print(f'{month}/{date}/{yr_2dig} is sequential')
else:
    print(f'{month}/{date}/{yr_2dig} is not sequential')