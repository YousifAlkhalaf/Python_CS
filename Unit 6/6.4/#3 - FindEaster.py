# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:36:34 2022

@author: Computer Science ~ B
"""

def find_easter(y):
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8*b + 13) // 25
    h = (19*a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (11*h + a) // 319
    r = (2*e + 2*j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h-m+r+n+19) % 32
    return (n, p, y) # month, day, year

def print_date(date):
    return_str = ''
    if date[0] == 3:
        return_str += 'March'
    elif date[0] == 4:
        return_str += 'April'
    else:
        return_str += 'ERROR'
    return_str += f' {date[1]}, {date[2]}'
    return return_str
    
year = int(input('What year would you like? '))
print(f'Easter Sunday: {print_date(find_easter(year))}')
