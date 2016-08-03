#!/usr/bin/env python

"""
@Author: Jordi Corbilla
@Description: Parallel MPI Matrix Multiplication (NxN)
"""

#from mpi4py import MPI
import sys

numberRows = 3
numberColumns = 3
TaskMaster = 0

A = [[0 for i in range(numberColumns)] for j in range(numberRows)]
B = [[0 for i in range(numberColumns)] for j in range(numberRows)]
C = [[0 for i in range(numberColumns)] for j in range(numberRows)]

def populateMatrix( p ):
    for i in range(0, numberRows):
        for j in range(0, numberColumns):
            p[i][j] = i+j

worldSize = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
processorName = MPI.Get_processor_name()

sys.stdout.write("Process %d started.\n" % (rank))
sys.stdout.write("Running from processor %s, rank %d out of %d processors.\n" % (processorName, rank, worldSize))

if rank == TaskMaster:
    sys.stdout.write("Initialising Matrix A and B (%d,%d).\n" % (numberRows, numberColumns))
    populateMatrix(A)
    populateMatrix(B)


for r in A:
   print(r)

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
