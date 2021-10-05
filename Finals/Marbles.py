# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:08:20 2021

@author: Computer Science ~ B
"""
# Make unbeatable AI two stars
# Fun but pretty easy

import random

ai_beatable = False
marbles = random.randint(2, 20)
marbles = 11
turn_num = 1

def human_turn(marbles):
    print('-Human player\'s turn!-')
    if marbles == 1:
        move = 1
    else:
        while True:
            move = input('How many marbles will you take away? ')
            if move.isdigit() and int(move) >= 1 and int(move) <= marbles // 2:
                move = int(move)
                break
            else:
                print('Invalid input')
    print(f'You take away {move} marbles')
    return move

def cpu_turn(marbles):
    print('-CPU turn!-')
    if ai_beatable:
        if marbles == 1:
            move = 1
        else:
            move = random.randint(1, marbles // 2)
    else:
        if marbles <= 3:
            move = 1
        else:
            i = marbles // 2
            if (marbles - i) % 2 != 0:
                move = i
            else:
                move = 1
    print(f'The CPU takes away {move} marbles')
    return move
    
    
while True:
    player_turn = input('Would you like to go first? ')
    player_turn = player_turn.lower()
    if player_turn == 'y' or player_turn == 'yes':
        player_turn = True
        break
    elif player_turn == 'n' or player_turn == 'no':
        player_turn = False
        break

while marbles > 0:
    
    print(f'\n<Turn {turn_num}>')
    print(f'--There are {marbles} marbles remaining--\n')
    move = 0
    if player_turn:
        move = human_turn(marbles)
        player_turn = False
    else:
        move = cpu_turn(marbles)
        player_turn = True
    marbles -= move
    turn_num += 1

if player_turn:
    print('PLAYER WINS')
else:
    print('CPU WINS')