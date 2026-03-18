#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:18:20 2026

@author: geoffreydesena

Exercises - day 3


"""

# %% Exericise 1

# part a - create a class called Person

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = str(self.first_name) + ' ' + str(self.last_name)
        
    def getFirstName(self):
        return self.first_name
    
    def getLastName(self):
        return self.last_name
           
    def __str__(self):
        return f"{self.full_name}"
        
# Test part a
Person1 = Person("Johan","Johansson")
print(Person1)

# Part b - create child class Student that takes Person methods and adds
# another method called subject
# concatenate name and subject in print function

class Student(Person):
    def __init__(self, first_name, last_name, subject):
        self.subject = subject
        super(Student, self).__init__(first_name,last_name)
        
    def getSubject(self, subject):
        return self.subject
    
    def printNameSubject(self):
        print(f"{self.full_name} {self.subject}")

# Test part b
Student1 = Student("Anders", "Andersson", "svenska")
Student1.printNameSubject()

# part d - create child class called teacher
class Teacher(Student):
    def __init__(self, first_name, last_name, subject):
        self.subject = subject
        super(Teacher, self).__init__(first_name,last_name,subject)
        
# Test part c
Teacher1 = Teacher("Sir","Robin","bravery")
Teacher1.printNameSubject()

# %% Exercise 2