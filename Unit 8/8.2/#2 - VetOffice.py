# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 13:52:50 2022

@author: Computer Science ~ B
"""

class Pet(object):
    id_num = 3001
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id_num = Pet.id_num
        Pet.id_num += 1
    
    def __str__(self):
        return f'{self.name}, age {self.age}  ID {self.id_num}'

def proceed_prompt():
    '''Y/N prompt for adding a pet'''
    while True:
        ans = input('Want to add a pet? ').upper()
        if ans == 'Y':
            return True
        elif ans == 'N':
            return False
        else:
            print('Invalid input. Try again.')
    

pets = []
add_more = True

while add_more:
    add_more = proceed_prompt()
    if (add_more):
        name = input('Enter name: ')
        age = input('Enter age, in years: ')
        pets.append(Pet(name, age))

for pet in pets:
    print(pet)