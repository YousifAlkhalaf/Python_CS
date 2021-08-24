# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:26:56 2021

@author: Computer Science ~ B
"""

# Turns card into integer    
def card_convert(card):
    if card == 'A' or card == 'a':
        card = int(11)
    elif card == 'K' or card == 'Q' or card == 'J' or card == 'k' or card == 'q' or card == 'j':
        card = int(10)
    else:
        card = int(card)
    return card

dealer_1 = input('Enter dealer\'s first card: ')
dealer_2 = input('Enter dealer\'s second card: ')
player_1 = input('Enter player\'s first card: ')
player_2 = input('Enter player\'s second card: ')

dealer_1 = card_convert(dealer_1)
dealer_2 = card_convert(dealer_2)
player_1 = card_convert(player_1)
player_2 = card_convert(player_2)

dealer = dealer_1 + dealer_2
player = player_1 + player_2

if dealer == 21 and player == 21:
    print('Both have blackjack: it\'s a draw')
elif player == 21:
    print('Player wins!')
elif dealer == 21:
    print('Dealer wins!')
else:
    print('No blackjacks!')