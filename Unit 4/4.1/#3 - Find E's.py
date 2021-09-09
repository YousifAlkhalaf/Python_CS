# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:10:44 2021

@author: Computer Science ~ B
"""

word = input('Enter a word: ')
e_count = 0
for i in range(len(word)):
    if word[i] == 'E' or word[i] == 'e':
        e_count += 1

print(f'The word {word} contains {e_count} E\'s')