# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:35:20 2021

@author: Computer Science ~ B
"""
# Very easy. One star difficulty
import random

def game1():
    for i in range (4):
        roll = random.randint(1, 6)
        if roll == 6:
            return True
    return False

def game2():
    for i in range (24):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        if roll2 == 6 and roll1 == 6:
            return True
    return False

def find_percent(wins, trials, r = 2):
    percent = wins/trials * 100
    percent = round(percent, r)
    return str(percent) + '%'

game1_wins = 0
game2_wins = 0

for i in range (100000):    
    if game1():
        game1_wins += 1

for i in range (100000):
    if game2():
        game2_wins += 1
        
print('|Game 1|Game 2|'.rjust(21))
print('Wins|'.rjust(7) + f'{game1_wins}'.center(6) + '|' + f'{game2_wins}'.center(6) + '|')
print('Losses|'.rjust(7) + f'{100000 - game1_wins}'.center(6) + '|' + f'{100000 - game2_wins}'.center(6) + '|')
print('Win %|'.rjust(7) + f'{find_percent(game1_wins, 100000)}'.center(6) + '|' + f'{find_percent(game2_wins, 100000)}'.center(6) + '|')