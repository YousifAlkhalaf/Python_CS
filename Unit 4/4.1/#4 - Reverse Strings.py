# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:24:32 2021

@author: Computer Science ~ B
"""

word = input('Enter a string: ')
reverse = ''
for i in range (len(word) - 1, -1, -1):
    reverse += word[i]
print(f'In reverse: {reverse}')