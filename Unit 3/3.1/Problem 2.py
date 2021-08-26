# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 13:34:55 2021

@author: Computer Science ~ B
"""

should_repeat = True
while should_repeat:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print(num1, 'plus', num2, 'is', num1+num2)
    response = input('Would you like to find another sum? Please enter "yes" to continue. ')
    if response != 'yes':
        should_repeat = False