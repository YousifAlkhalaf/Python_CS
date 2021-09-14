# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:41:19 2021

@author: Computer Science ~ B
"""

word = input('Enter a word: ')
new_word = word[len(word)//2: len(word)] + word[0: len(word)//2]
print(f'New word: {new_word}')