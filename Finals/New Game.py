# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:04:15 2021

@author: Computer Science ~ B
"""

import random

# 3 rolls from greatest to least
def game1():
    max = 6
    for i in range(3):
        roll = random.randint(1, 6)
        if roll > max:
            return False
        else:
            max = roll
    return True

# 3 rolls from least to greatest
def game2():
    min = 1
    for i in range (3):
        roll = random.randint(1, 6)
        if roll < min:
            return False
        else:
            min = roll
    
    return True

def find_percent(wins, trials, r = 2):
    percent = wins/trials * 100
    percent = round(percent, r)
    return str(percent) + '%'

game1_wins = 0
game2_wins = 0

for i in range (10000):    
    if game1():
        game1_wins += 1

for i in range (10000):
    if game2():
        game2_wins += 1
        
print('|Game 1|Game 2|'.rjust(21))
print('Wins|'.rjust(7) + f'{game1_wins}'.center(6) + '|' + f'{game2_wins}'.center(6) + '|')
print('Losses|'.rjust(7) + f'{100000 - game1_wins}'.center(6) + '|' + f'{100000 - game2_wins}'.center(6) + '|')
print('Win %|'.rjust(7) + f'{find_percent(game1_wins, 100000)}'.center(6) + '|' + f'{find_percent(game2_wins, 100000)}'.center(6) + '|')