# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 14:02:33 2022

@author: Computer Science ~ B
"""

def SixStuff(a, b) :
   if a == 6 or b == 6:
       return True
   elif a + b == 6:
       return True
   elif a - b == 6 or b - a == 6:
       return True
   return False

#Return True
print(SixStuff(6, 3))
print(SixStuff(8, 2))
print(SixStuff(1, 5))

#Return False
print(SixStuff(1, 1))
print(SixStuff(10, 5))