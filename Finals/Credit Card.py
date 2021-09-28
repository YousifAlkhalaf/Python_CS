# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:09:38 2021

@author: Computer Science ~ B
"""
# Credit Card
# Decently challenging, interesting
import math

def find_digit_sum(num, step = 1):
    sum = 0
    i = 0
    while num > 0:
        if i % step == 0:
            sum += num % 10
        num //= 10
        i += 1
    return sum

def digits_greater_than(num)
        
while True:
    card_num = input('Enter your card number: ')
    card_num = card_num.replace(' ', '')
    if len(card_num) == 16:
        if card_num.isdigit():
            card_num = int(card_num)
            break
    print('Invalid input. Try again.')

full_digit_sum = find_digit_sum(card_num)
odd_digit_num = find_digit_sum(card_num, 2)
greater_than_4 = digits_greater_than()