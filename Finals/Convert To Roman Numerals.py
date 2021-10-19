# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:08:05 2021

@author: Computer Science ~ B
"""
# Not that hard. One star... maybe two stars

def find_roman(num) :
    new_num = ''
    while num // 1000 > 0:
        new_num += 'M'
        num -= 1000
    
    if num // 500 == 1:
        new_num += 'D'
        num -= 500
    while num // 100 > 0:
        new_num += 'C'
        num -= 100
        
    new_num = new_num.replace('DCCCC', 'CM')
    
    if num // 50 == 1:
        new_num += 'L'
        num -= 50
    while num // 10 > 0:
        new_num += 'X'
        num -= 10
    
    new_num = new_num.replace('LXXXX', 'XC')
    
    if num // 5 == 1:
        new_num += 'V'
        num -= 5
    while num // 1 > 0:
        new_num += 'I'
        num -= 1
    
    new_num = new_num.replace('VIIII', 'IX')
    new_num = new_num.replace('IIII', 'IV')
    
    return new_num
    
while True:
    num = input('Enter a positive integer: ')
    if num.isalnum() and int(num) < 4000:
        num = int(num)
        break
    else:
        print('Invalid input. Try again.')

print(find_roman(num))