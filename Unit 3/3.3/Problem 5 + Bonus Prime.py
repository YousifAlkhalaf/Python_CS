# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:14:06 2021

@author: Computer Science ~ B
"""

def find_prime (num):
    for i in range (2, num, 1):
        if i == 1 or num % i == 0:
            return False
    return True


n = int(input('Enter a positive integer: '))
if find_prime(n):
    print('The number is prime')
else:
    print('The number is not prime')
    
print('\nFIRST 100 PRIME NUMBERS\n')
num = 2
counter = 1
while counter <= 100:
    if find_prime(num):
        print(f'{counter}. {num}')
        counter += 1
    num += 1