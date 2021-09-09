# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:53:29 2021

@author: Computer Science ~ B
"""
is_all_nums = False
value = input('Enter a number: ')

while is_all_nums == False:
    if value.isnumeric() == False:
        value = input('I don\'t recognize that number. Enter a number: ')
    else:
        num = int(value)
        is_all_nums = True
    
print(f'Thank you.\nYour number is {num}')