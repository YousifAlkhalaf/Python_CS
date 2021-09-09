# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:49:06 2021

@author: Computer Science ~ B
"""

word = input('Enter a string: ')
word = word.lower()
vowels = 0

for i in range (len(word)):
    if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
        vowels += 1
print(f'Number of vowels: {vowels}')