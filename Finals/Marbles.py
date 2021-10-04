# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:08:20 2021

@author: Computer Science ~ B
"""
import random

ai_beatable = True
marbles = random.randint(2, 20)
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
            else:
                print('Invalid input')
    print(f'You take away {move} pebbles')
    return move

def cpu_turn(marbles):
    print('-CPU turn!-')
    if ai_beatable:
        if marbles == 1:
            move = 1
        else:
            move = random.randint(1, marbles // 2)
    print(f'The CPU takes away {move} pebbles')
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
    
    print(f'<Turn {turn_num}>')
    print(f'--There are {marbles} marbles remaining--\n')
    
    if player_turn:
        move = human_turn(marbles)
    elif player_turn != True:
        move = cpu_turn()
    marbles -= move
    player_turn != player_turn
    turn_num += 1
        