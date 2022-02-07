# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:47:38 2022

@author: Computer Science ~ B
"""
# Problem 2
d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50,6:60}
d4 = {}
d4.update(d1)
d4.update(d2)
d4.update(d3)
print(d4)

# Problem 3
for key,val in d4.items():
    print(f'{key} times ten is {val}')

# Problem 4
print(sum(d4.values()))