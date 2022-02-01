# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:50:39 2022

@author: Computer Science ~ B
"""

def can_spell(old_word, new_word):
    old_word = list(old_word)
    new_word = list(new_word)
    for char in new_word:
        if old_word.count(char) < new_word.count(char):
            return False
    return True

def loop(old_word):
    ans = ''
    while ans != 'q':
        ans = input('Enter another word (or \'q\' to quit): ')
        if ans == 'q':
            return
        elif can_spell(old_word, ans):
            print(f'Yes, {ans} can be spelled from {old_word}')
        else:
            print(f'{ans} cannot be spelled from {old_word}')
    

old_word = input('What is the starting word? ')
loop(old_word)
