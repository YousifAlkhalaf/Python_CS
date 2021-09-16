# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:27:08 2021

@author: Computer Science ~ B
"""

word = input('Enter a word or phrase: ')
for i in range (len(word)):
    if i % 2 == 0:
        print(word[i], end = '')
    else:
        print(end = '')