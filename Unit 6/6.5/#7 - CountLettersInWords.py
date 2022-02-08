# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 13:33:21 2022

@author: Computer Science ~ B
"""

def count_unique(word):
    letter_cnt = {}
    for let in word:
        letter_cnt[let] = word.count(let)
    return letter_cnt

word = input('Enter a word: ')
print(count_unique(word))