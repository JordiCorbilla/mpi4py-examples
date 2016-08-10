#!/usr/bin/env python

"""
@Author: Jordi Corbilla
@Description: Parallel MPI Matrix Multiplication (NxN)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from mpi4py import MPI
import sys
import numpy as np

numberRows = int( sys.argv[1])
numberColumns = int( sys.argv[2])
TaskMaster = 0

assert numberRows == numberColumns

print ("Initialising variables.\n")
a = np.zeros(shape=(numberRows, numberColumns))
b = np.zeros(shape=(numberRows, numberColumns))
c = np.zeros(shape=(numberRows, numberColumns))

def populateMatrix( p ):
    for i in range(0, numberRows):
        for j in range(0, numberColumns):
            p[i][j] = i+j

comm = MPI.COMM_WORLD
worldSize = comm.Get_size()
rank = comm.Get_rank()
processorName = MPI.Get_processor_name()

print ("Process %d started.\n" % (rank))
print ("Running from processor %s, rank %d out of %d processors.\n" % (processorName, rank, worldSize))

#Calculate the slice per worker
if (worldSize == 1):
    slice = numberRows
else:
    slice = numberRows / (worldSize-1) #make sure it is divisible

assert slice >= 1

populateMatrix(b)

comm.Barrier()
    
if rank == TaskMaster:
    print ("Initialising Matrix A and B (%d,%d).\n" % (numberRows, numberColumns))
    populateMatrix(a)
        
    for i in range(1, worldSize):
        offset = (i-1)*slice #0, 10, 20
        row = a[offset,:]
        comm.send(offset, dest=i, tag=i)
        comm.send(row, dest=i, tag=i)
        for j in range(0, slice):
            comm.send(a[j+offset,:], dest=i, tag=j+offset)
    print ("All sent to workers.\n")

comm.Barrier()

if rank != TaskMaster:

    print ("Data Received from process %d.\n" % (rank))
    offset = comm.recv(source=0, tag=rank)
    recv_data = comm.recv(source=0, tag=rank)
    for j in range(1, slice):
        c = comm.recv(source=0, tag=j+offset)
        recv_data = np.vstack((recv_data, c))

    print ("Start Calculation from process %d.\n" % (rank))

    #Loop through rows
    t_start = MPI.Wtime()
    for i in range(0, slice):
        res = np.zeros(shape=(numberColumns))
        if (slice == 1):
            r = recv_data
        else:
            r = recv_data[i,:]
        ai = 0
        for j in range(0, numberColumns):
            q = b[:,j] #get the column we want
            for x in range(0, numberColumns):
                res[j] = res[j] + (r[x]*q[x])
            ai = ai + 1
        if (i > 0):
           send = np.vstack((send, res))
        else:
            send = res
    t_diff = MPI.Wtime() - t_start
    
    print("Process %d finished in %5.4fs.\n" %(rank, t_diff))
    #Send large data
    print ("Sending results to Master %d bytes.\n" % (send.nbytes))
    comm.Send([send, MPI.FLOAT], dest=0, tag=rank) #1, 12, 23

comm.Barrier()

if rank == TaskMaster:  
    print ("Checking response from Workers.\n")
    res1 = np.zeros(shape=(slice, numberColumns))
    comm.Recv([res1, MPI.FLOAT], source=1, tag=1)
    print ("Received response from 1.\n")
    kl = np.vstack((res1))
    for i in range(2, worldSize):
        resx= np.zeros(shape=(slice, numberColumns))
        comm.Recv([resx, MPI.FLOAT], source=i, tag=i)
        print ("Received response from %d.\n" % (i))
        kl = np.vstack((kl, resx))

    print ("Result AxB.\n")
    print (kl)   

comm.Barrier()