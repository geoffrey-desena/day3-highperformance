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

# %% Exercise 2 - NumPy

import numpy as np

#### a. Create a null vector of size 10 but the fifth value which is 1

vecA = np.zeros(10,dtype=int)
vecA[4] = 1
print(f"Part a: \n {vecA} \n")

#### b. Create a vector with values ranging from 10 to 49
vecB = np.arange(10, 49)
print(f"Part b: \n {vecB} \n")

#### c. Reverse a vector (first element becomes last) 
vecC = np.arange(10)
print(f"Part c forward: \n {vecC}\n")

vecCrev = np.flip(vecC)
print(f"Part c backward: \n {vecCrev}\n")


#### d. Create a 3x3 matrix with values ranging from 0 to 8
vecD = np.arange(9).reshape(3,3)
print(f"Part d: \n {vecD}\n")


#### e. Find indices of non-zero elements from [1,2,0,0,4,0]
vecE = np.array([1,2,0,0,4,0])
bool_nonzero = vecE != 0
idx_nonzero = np.arange(len(vecE))[bool_nonzero]
print(f"Part e: \n Indices are: {idx_nonzero}\n")


#### f. Create a random vector of size 30 and find the mean value
vecF = np.random.random(30)
print(f"Part f:\nRando vector: {vecF}")
vecFmean = vecF.mean()
print(f"Rando vector mean: {vecFmean}\n")


#### g. Create a 2d array with 1 on the border and 0 inside
vecG = np.zeros((4,4),dtype=int)
vecG[0,:] = 1
vecG[-1,:] = 1
vecG[:,0] = 1
vecG[:,-1] = 1
print(f"Part g:\n2d array with 1s on the border: \n {vecG}\n")


#### h. Create a 8x8 matrix and fill it with a checkerboard pattern
vecH = np.zeros((8,8),dtype=int)
s1 = slice(0,len(vecH),2)
s2 = slice(1,len(vecH) ,2)
vecH[s1,s1] = 1
vecH[s2,s2] = 1
print(f"Part h:\n Checkerboarded 8x8: \n {vecH}\n")

#### i. Create a checkerboard 8x8 matrix using the tile function
# Chat tells me to start with a small block and then repeat
vector_seed = np.array([[1,0],[0,1]])
vecI = np.tile(vector_seed,(4,4))
print(f"Part i:\n Should look identical to part h: \n {vecI}")

#### j. Given a 1D array, negate all elements which are between 3 and 8, in place
vecJ = np.arange(11)
mask = (vecJ > 3) & (vecJ < 8)
vecJ[mask]*=-1
print(f"Part j: \n {vecJ}\n")


#### k. Create a random vector of size 10 and sort it
vecK = np.random.random(10)
print(f"Part k: \n {np.sort(vecK)}\n")

#### l. Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = A == B
print(f"Part l: \n A: {A} \n B: {B}")
print(f"The two vectors are equal: {np.all(equal)}\n")

#### m. How to calculate the square of every number in an array in place (without creating temporaries)?

vecM = np.arange(10, dtype=np.int32)**2
print(f"Part m: \n {vecM}\n")

#### n. How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
print("At this point, I can just guess that the function is called 'diagonal'")
print(f"{np.diagonal(C)}")
print("oh, hey! woodja look at that!")

# %% Exercise 3
# Revisit the ```matmult.py``` example from yesterday and improve its performance using Numpy.

# Well, I didn't get that far yesterday, so let's see.
# np must have a function for this...

N = 100
Mat1 = np.random.rand(N,N)
Mat2 = np.random.rand(N,N+1)

prod = np.matmul(Mat1,Mat2)
print(f"The result has dimensions {prod.shape}")

# %% Exercise 4: MPI parallelization

# Geinuinely doubting that I'll ever need this... I'm skipping it for now

#### a. Write a simple MPI script ```mpi_ranks.py``` that prints the rank of the different processes when running 

# mpirun python mpi_ranks.py

# #### b. Write a small script ```mpi_sum.py``` which calculates the sum over all ranks and prints the result from the process with rank 0.
# Hint: Have a look at the tutorials from the mpi4py documentation page: [https://mpi4py.readthedocs.io/en/stable/tutorial.html](https://mpi4py.readthedocs.io/en/stable/tutorial.html)

# %% Exercise 5

# Also seems beyond my needs.
# I'm going back to the Day 2 exercises


