# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:04:40 2021

@author: Computer Science ~ B
"""

# GPA calculator
# One star. Easy, but boring and not engaging

def calculate_class(grade, is_honors):
    if grade == 'A':
        points = 4
    elif grade == 'B':
        points = 3
    elif grade == 'C':
        points = 2
    elif grade == 'D':
        points = 1
    else:
        points = 0
        
    if points >= 2 and is_honors:
        points += 1
    return points

def find_GPA(grade_num, total_points):
    return total_points/grade_num

repeat = True
total_points = 0
grade_num = 0

while repeat:
    while True:
        grade = input('Enter your letter grade for a class: ')
        grade = grade.upper()
        if grade == 'A' or grade == 'B' or grade == 'C' or grade == 'D' or grade == 'F':
            break
        else:
            print('Invalid input. Try again')
    
    while True:
        is_honors = input('Is this an honors or AP Course? Type Yes or No: ')
        is_honors = is_honors.lower()
        if is_honors == 'yes':
            is_honors = True
            break
        elif is_honors == 'no':
            is_honors = False
            break
        else:
            print('Invalid input. Try again.')
    
    class_points = calculate_class(grade, is_honors)
    grade_num += 1
    total_points += class_points
    gpa = find_GPA(grade_num, total_points)
    print()
    print(f'''You got {class_points} in your class!
Your GPA is now {gpa}.''')
    
    while True:
        repeat = input('Would you like to input another grade? ')
        repeat = repeat.lower()
        if repeat == 'no':
            repeat = False
            break
        elif repeat == 'yes':
            break
        else:
            print('Invalid input. Try again.')