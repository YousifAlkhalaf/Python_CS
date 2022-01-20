# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:03:25 2022

@author: Computer Science ~ B
"""

word = str(input('Enter a string: ')).lower()
word = word.replace(' ', '')
new_word = ''
for c in word:
    if new_word.find(c) == -1:
        new_word += c
print(new_word)
    
    
        