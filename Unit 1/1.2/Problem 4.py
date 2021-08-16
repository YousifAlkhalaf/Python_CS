# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:56:32 2021

@author: Computer Science ~ B
"""

book_num = int(input('How many books will be ordered? '))
book_cost = 24.95
base_ship_fee = 3
added_ship_fee = 0.75
discount = 0.4

cost = (book_num * (book_cost * (1-discount))) + base_ship_fee + (added_ship_fee * (book_num - 1))
cost = round(cost, 2)
        
print(f'Total cost is ${cost}')