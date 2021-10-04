# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:09:38 2021

@author: Computer Science ~ B
"""
# Credit Card
# Decently challenging, interesting
import math

def find_digit_sum(num, step = 1, start = 0):
    sum = 0
    i = start
    while num > 0:
        digit = num % 10
        if i % step == 0:
            sum += digit
        num //= 10
        i += 1
    return sum

def greater_than_x(num, min_digit):
    count = 0
    while num > 0:
        digit = num % 10
        if digit > 4:
            count += 1
        num //= 10
    return count

def every_other_digit(num, start = 0):
    num = str(num)
    new_num = ''
    for i in range (start, len(num), 2):
        new_num += num[i]
    return int(new_num)

def is_valid(full_digit_sum, odd_digit_sum, greater_than_4):
   sum = full_digit_sum + odd_digit_sum + greater_than_4
   if sum % 10 == 0:
       return True
   else:
       return False
        
while True:
    card_num = input('Enter your card number: ')
    card_num = card_num.replace(' ', '')
    if len(card_num) == 16:
        if card_num.isdigit():
            card_num = int(card_num)
            break
    print('Invalid input. Try again.')

full_digit_sum = find_digit_sum(card_num)
odd_digit_sum = find_digit_sum(card_num, 2, 1)
greater_than_4 = greater_than_x(every_other_digit(card_num), 4)

#print(full_digit_sum)
#print(odd_digit_sum)
#print(greater_than_4)
#print(every_other_digit(card_num))

if is_valid(full_digit_sum, odd_digit_sum, greater_than_4):
    print('The card is valid')
else:
    print('You\'re under arrest')