# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:53:13 2022

@author: Computer Science ~ B
"""

def tuples_to_dicts(students):
    '''Student tuple to dictionary'''
    new_students = []
    for student in students:
        new_student = {'name': student[0], 'grade': student[1], 'GPA': student[2]}
        new_students.append(new_student)
    return new_students

def highest_gpa(students):
    '''Finds highest GPA per grade'''
    total_students = sort_by_grade(students)
    best_students = []
    for grade in total_students.values():
        max_gpa = -1
        student_index = -1
        for i in range(len(grade)):
            student = grade[i]
            if student['GPA'] > max_gpa:
                max_gpa = student['GPA']
                student_index = i
        best_students.append(grade[student_index])
    return best_students
        
def sort_by_grade(students):
    '''Creates dictionary with lists of students per grade'''
    grade_list = {}
    for student in students:
        grade = student['grade']
        if grade_list.get(grade) == None:
            grade_list.update({grade: []})
        grade_list[grade].append(student)
    return grade_list
        
print('Starting student list\n')
students = [('Rivera', 12, 4.056), ('Johnson', 11, 3.987), ('Cabrera', 12, 4.100), ('Michaels', 12, 3.336), ('Miller', 12, 3.998), ('Sanders', 11, 3.998)]
print(students)
print('\nTuples to dictionaries\n')
students = tuples_to_dicts(students)
print(students)
print('\nHighest GPA per grade\n')
print(highest_gpa(students))