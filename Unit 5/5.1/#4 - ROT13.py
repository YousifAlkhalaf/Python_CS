# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:26:18 2021

@author: Computer Science ~ B
"""

def rotate_word(word, factor):
    new_word = ''
    for c in word:
        tmp1 = ord(c)
        if tmp1 + factor > ord('z'):
            tmp2 = chr((tmp1 + factor) - 26)
        else:
            tmp2 = chr(tmp1 + factor)
        new_word += tmp2
    return new_word

word = input('What is the word? ')
num = int(input('What is the number of steps in rotation? '))
print(f'The new word is {rotate_word(word, num)}')