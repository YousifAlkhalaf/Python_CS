# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 13:39:21 2021

@author: Computer Science ~ B
"""

rows = 0
columns = 0
while rows < 1:
    rows = int(input('How many rows will the rectangle have? '))
while columns < 1:
    columns = int(input('How many columns will the rectangle have? '))
    
print(f'Here is your {rows} X {columns} rectangle: ')

#Standard execution
#for h in range (0, rows, 1):
#   for w in range (0, columns, 1):
#        print('#', end = ' ')
#   print()

# One-loop  
for i in range (1, rows * columns + 1, 1):
    print('#', end = ' ')
    if i % columns == 0:
        print()