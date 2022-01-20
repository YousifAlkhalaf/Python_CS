# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 14:36:16 2022

@author: Computer Science ~ B
"""
def printData(days, daily_rate, total):
    '''Returns a string formatted to my data table'''
    return_str = ''
    
    days = str(int(days))
    daily_rate = '{:.2f}'.format(daily_rate)
    total = '{:.2f}'.format(total)
    
    return_str += days.rjust(5) + '  |'
    return_str += daily_rate.rjust(12) + '    |'
    return_str += total.rjust(13)
    return return_str
    
    
print('days'.center(7) + '|' + 'daily rate ($)'.center(16) + '|' + 'total to date ($)'.center(19))
print('____________________________________________')
day = 1
start = 0.01
total = 0

while total < 1000000:
    daily_rate = start * (2 ** (day-1))
    total += daily_rate
    print(printData(day, daily_rate, total))
    day += 1
