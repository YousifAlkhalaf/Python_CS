# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:36:53 2021

@author: Computer Science ~ B
"""

word = input('Enter a word: ')
letter = input('Enter a letter: ')
word = word.replace(letter, '')
print(f'New word: {word}')