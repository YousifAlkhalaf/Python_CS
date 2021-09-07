# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:32:55 2021

@author: Computer Science ~ B
"""

integer = 0
while integer % 2 == 0:
    integer = int(input('Enter an odd, positive integer: '))

print('SQUARE')
for s in range(1, integer**2+1, 1):
    print(f'* ', end = '')
    if s % integer == 0:
        print()

print('\nTRIANGLE')
for i in range (1, integer+1, 1):
    for k in range (0, i, 1):
        print('*', end = ' ')
    print()

print('\nPINE TREE')
for spaces in range ((integer - 1)//2, -1, -1):
    for i in range (spaces, 0, -1):
        print('  ', end = '')
    for x in range (integer - (2 * spaces), 0, -1):
        print('*', end = ' ')
    for i in range (spaces, 0, -1):
        print(' ', end = '')
    print()
for k in range ((integer - 1) // 2, 0, -1):
    print('  ', end = '')
print ('#')