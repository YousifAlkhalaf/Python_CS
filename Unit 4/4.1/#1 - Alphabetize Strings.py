# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:22:30 2021

@author: Computer Science ~ B
"""

s1 = input('Enter a string (all lowercase!!!): ')
s2 = input('Enter a string (all lowercase!!!): ')
s3 = input('Enter a string (all lowercase!!!): ')
print()

if s1 < s2 and s1 < s3:
    print(s1)
    if s2 < s3:
        print(s2)
        print(s3)
    else:
        print(s3)
        print(s2)
elif s2 < s1 and s2 < s3:
    print(s2)
    if s1 < s3:
        print(s1)
        print(s3)
    else:
        print(s3)
        print(s1)
else:
    print(s3)
    if s1 < s2:
        print(s1)
        print(s2)
    else:
        print(s2)
        print(s1)