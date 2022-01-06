# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:08:28 2022

@author: Computer Science ~ B
"""

score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
test_total = float(input("Enter test total: "))

score1_percent = round(score1/test_total * 100, 2)
print(f'Test 1: {score1_percent}')
score2_percent = round(score2/test_total * 100, 2)
print(f'Test 2: {score2/test_total * 100}')
score3_percent = round(score3/test_total * 100, 2)
print(f'Test 3: {score3/test_total * 100}')

avg = score1_percent + score2_percent + score3_percent
avg /= 3
avg = round(avg, 2)
print(f'Test average is {avg}')