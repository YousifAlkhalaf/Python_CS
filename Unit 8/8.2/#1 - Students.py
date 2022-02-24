# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 13:40:43 2022

@author: Computer Science ~ B
"""
class Student(object):
    def __init__(self, last, first, grade, id_num):
        self.last = last
        self.first = first
        self.grade = grade
        self.id_num = id_num
    
    def __str__(self):
        return f'{self.last} {self.first}, grade {self.grade} ID: {self.id_num}'

students = []
with open('students.txt', 'r') as f:
    for line in f:
        info = line.split()
        last = info[0]
        first = info[1]
        grade = info[2]
        id_num = info[3]
        
        students.append(Student(last, first, grade, id_num))

for student in students:
    print(student)


        