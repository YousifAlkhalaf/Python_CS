# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:03:48 2021

@author: Computer Science ~ B
"""

go_again = True
while go_again:
    name = input('What is your name? ')
    print(f'Hello {name}\n')
    go = input('Would you like to go again? ')
    if go == 'no':
        print(f'Goodbye {name}')
        go_again = False