# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:10:32 2022

@author: Computer Science ~ B
"""

def guest_list(list1, list2, list3):
    guest_list = list1.union(list2.union(list3))
    print(f'Number of guests: {len(guest_list)}')
    print(f'Guest list: {guest_list}')

your_list = {'Britney', 'Amber', 'Freddie', 'Monica', 'Evan'}
bro_list = {'Charlie', 'Andy', 'Becca', 'Sam', 'Freddie'}
friend_list = {'Becca', 'Freddie', 'Sam', 'Miguel', 'Evan'}

guest_list(your_list, bro_list, friend_list)