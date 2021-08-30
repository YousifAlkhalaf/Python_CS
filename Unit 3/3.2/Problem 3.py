# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:14:19 2021

@author: Computer Science ~ B
"""
sum = 0
for num in range(1, 11, 1):
    sum += num/(11-num)
    print(f'{num}/{11-num}')
print('Sum is {}'.format(sum))