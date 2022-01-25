# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 13:14:41 2022

@author: Computer Science ~ B
"""

def caterPrice(sandwiches, salads, sodas):
    total = 0
    total += int(sandwiches) * 5.99
    total += int(salads) * 4.50
    total += int(sodas) * 1.50
    total = '{:.2f}'.format(total)
    return f'Your total is ${total}'

value = caterPrice(2, 4, 2)
print('caterPrice(2, 4, 2)')
print('Expected output: Your total is $11.99')
print(f'Output: {value}\n')
value = caterPrice(0, 0, 4)
print('caterPrice(0, 0, 4)')
print('Expected output: Your total is $6.00')
print(f'Output: {value}\n')
value = caterPrice(5, 4, 3)
print('caterPrice(5, 4, 3)')
print('Expected output: Your total is $52.45')
print(f'Output: {value}\n')
