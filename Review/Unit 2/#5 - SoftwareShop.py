# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:35:25 2022

@author: Computer Science ~ B
"""
import math

def findDiscount(num_bought):
    '''Calculates the discount given'''
    if num_bought >= 10 and num_bought <= 19:
        return 0.8
    elif num_bought >= 20 and num_bought <= 49:
        return 0.7
    elif num_bought >= 50 and num_bought <= 99:
        return 0.6
    elif num_bought > 99:
        return 0.5
    else:
        return 1

def findCost(num_bought, pack_price, discount):
    '''Calculates end cost'''  
    return (num_bought * pack_price) * discount
    

pack_price = 99
num_bought = int(input('Enter the number of packages purchased: '))

#Find discount
discount = findDiscount(num_bought)
discount_percent = int((1-discount) * 100)
cost = findCost(num_bought, pack_price, discount)
print(f'Your discount is {discount_percent}%')
print('Your cost is ${:.2f}'.format(cost))

#MPC extra
new_amt = math.ceil(num_bought/10) * 10
new_cost = findCost(new_amt, pack_price, findDiscount(new_amt))

old_overall = cost/num_bought
new_overall = new_cost/new_amt
if new_overall < old_overall:
    savings = (old_overall * num_bought - new_overall * new_amt)
    more_packs = new_amt - num_bought
    print('If you purchase {} more package(s), you will save ${:.2f}'.format(more_packs, savings))
    
    
    
    