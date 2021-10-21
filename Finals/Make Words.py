# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:01:19 2021

@author: Computer Science ~ B
"""
#Quite easy. One star
import random

def randvowel(word):
    num = random.randint(1, 5)
    if num == 1:
        return word + 'a'
    elif num == 2:
        return word + 'e'
    elif num == 3:
        return word + 'i'
    elif num == 4:
        return word + 'o'
    elif num == 5:
        return word + 'u'

def randcons(word):
    num = random.randint(1, 21)
    if num == 1:
        return word + 'b'
    elif num == 2:
        return word + 'c'
    elif num == 3:
        return word + 'd'
    elif num == 4:
        return word + 'f'
    elif num == 5:
        return word + 'g'
    elif num == 6:
        return word + 'h'
    elif num == 7:
        return word + 'j'
    elif num == 8:
        return word + 'k'
    elif num == 9:
        return word + 'l'
    elif num == 10:
        return word + 'm'
    elif num == 11:
        return word + 'n'
    elif num == 12:
        return word + 'p'
    elif num == 13:
        return word + 'q'
    elif num == 14:
        return word + 'r'
    elif num == 15:
        return word + 's'
    elif num == 16:
        return word + 't'
    elif num == 17:
        return word + 'z'
    elif num == 18:
        return word + 'v'
    elif num == 19:
        return word + 'w'
    elif num == 20:
        return word + 'x'
    elif num == 21:
        return word + 'y'


word = ''
for i in range(0, 3, 1):
    word = randvowel(word)
for i in range(0, 5, 1):
    word = randcons(word)

print(word)

stop = False
counter = 0

while stop == False:   
    print('Valid words:', counter)
    new_word = input('Enter a word with the characters provided above. Enter "X" to quit: ')
    
    if new_word == 'X':
        stop = True
        print('Goodbye!')
    else:
        new_word = new_word.lower()
        is_valid = True
        
        for c in new_word:
            old_count = word.count(c)
            if new_word.count(c) > old_count:
                is_valid = False
                
        if is_valid:
            counter += 1
        else:
            print('Invalid word.')
    