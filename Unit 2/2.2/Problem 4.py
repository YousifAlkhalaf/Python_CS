# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:26:56 2021

@author: Computer Science ~ B
"""

dealer_1 = input('Enter dealer\'s first card: ')
dealer_2 = input('Enter dealer\'s second card: ')
player_1 = input('Enter player\'s first card: ')
player_2 = input('Enter player\'s second card: ')

if player_1 == 'A':
    player_1 = int(11)
elif player_1 == 'K' or player_1 == 'Q' or player_1 == 'J':
    player_1 = int(10)
else:
    player_1 = int(player_1)