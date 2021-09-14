# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:20:09 2021

@author: Computer Science ~ B
"""

word = input('Enter a word: ')
new_word = word[0: len(word): 2]

print(f'Every other letter: {new_word}')