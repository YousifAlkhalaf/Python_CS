# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 13:04:33 2022

@author: Computer Science ~ B
"""

guesses = set()
while len(guesses) < 4:
    guess = input(f'Guess a letter!: Guess {len(guesses)+1}: ')
    if {guess}.issubset(guesses):
        print('You have guessed that letter already. Guess again!')
    else:
        guesses.add(guess)
print(f'Final guesses: {guesses}')