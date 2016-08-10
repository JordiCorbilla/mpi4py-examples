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

a = np.zeros(shape=(numberRows, numberColumns))
b = np.zeros(shape=(numberRows, numberColumns))
c = np.zeros(shape=(numberRows, numberColumns))

##A = [[0 for i in range(numberColumns)] for j in range(numberRows)]
##B = [[0 for i in range(numberColumns)] for j in range(numberRows)]
##C = [[0 for i in range(numberColumns)] for j in range(numberRows)]

def populateMatrix( p ):
    for i in range(0, numberRows):
        for j in range(0, numberColumns):
            p[i][j] = i+j

comm = MPI.COMM_WORLD
worldSize = comm.Get_size()
rank = comm.Get_rank()
processorName = MPI.Get_processor_name()

sys.stdout.write("Process %d started.\n" % (rank))
sys.stdout.write("Running from processor %s, rank %d out of %d processors.\n" % (processorName, rank, worldSize))

#Calculate the slice per worker
if (worldSize == 1):
    slice = numberRows
else:
    slice = numberRows / (worldSize-1) #make sure it is divisible

populateMatrix(b)

comm.Barrier()
    
if rank == TaskMaster:
    sys.stdout.write("Initialising Matrix A and B (%d,%d).\n" % (numberRows, numberColumns))
    populateMatrix(a)
    #populateMatrix(b)

    #print("matrix A")
    #print(a)
    #print ("matrix B")
    #print (b)
    
    
    for i in range(1, worldSize):
        offset = (i-1)*slice #0, 10, 20
        row = a[offset,:]
        comm.send(offset, dest=i, tag=i)
        #comm.send(b, dest=i, tag=i)
        comm.send(row, dest=i, tag=i)
        for j in range(0, slice):
            comm.send(a[j+offset,:], dest=i, tag=j+offset)
            #print("sending to " + str(i))
            #print(a[j+offset,:])
            #row = np.vstack((row, a[j+offset,:]))
        
        
        #print("sent")
        
    #row1 = a[0,:]
    #row2 = a[1,:]
    #row3 = a[2,:]
    #Sending data
    #comm.send(row1, dest=1, tag=1)
    #comm.send(b, dest=1, tag=1)
    #comm.send(row2, dest=2, tag=2)
    #comm.send(b, dest=2, tag=2)
    #comm.send(row3, dest=3, tag=3)
    #comm.send(b, dest=3, tag=3)
    print ("all sent")

comm.Barrier()

if rank != TaskMaster:
    #comm.Barrier()
    #for i in range(1, worldSize):
    print ("received")
    offset = comm.recv(source=0, tag=rank)
    #b = comm.recv(source=0, tag=rank)
    recv_data = comm.recv(source=0, tag=rank)
    for j in range(1, slice):
        c = comm.recv(source=0, tag=j+offset)
        recv_data = np.vstack((recv_data, c))

    print ("calculation")
    #Perform calculations

    #Loop through rows
    t_start = MPI.Wtime()
    for i in range(0, slice):
        res = np.zeros(shape=(numberColumns))
        if (slice == 1):
            r = recv_data
            print (r)
        else:
            r = recv_data[i,:]
        ai = 0
        #if (rank == 1):
        #    print ("r")
        #    print (r)
        for j in range(0, numberColumns):
            q = b[:,j] #get the column we want
            #if (rank == 1):
            #    print ("q")
            #    print (q)
            for x in range(0, numberColumns):
                res[j] = res[j] + (r[x]*q[x])
            #if (rank == 1):
            #    print ("res")
            #    print (res)
            ai = ai + 1
        if (i > 0):
           send = np.vstack((send, res))
        else:
            send = res
    t_diff = MPI.Wtime() - t_start
    print(" process %d finished in %5.4fs" %(rank, t_diff))
    #Send large data
    print ("Sending results " + str(send.nbytes))
    comm.Send([send, MPI.FLOAT], dest=0, tag=rank) #1, 12, 23

    #print ("Sending results")
    #comm.send(offset, dest=0, tag=rank)
    #for i in range(0, slice):
    #    print ("sending to master " + str(rank+i+offset) )
    #    comm.send(send[i,:], dest=0, tag=rank+i+offset) #1, 12, 23

comm.Barrier()

if rank == TaskMaster:
    #Receiving response
    #print ("receiving response 1")
    #offset1 = comm.recv(source=1, tag=1)
    #print ("receiving response " + str(1+offset1))
    #res1 = comm.recv(source=1, tag=1+offset)
    #for i in range(1, slice):
    #    c = comm.recv(source=1, tag=1+i+offset)
    #    res1 = np.vstack((res1, c))

    #print ("receiving response 2")    
    #offset2 = comm.recv(source=2, tag=2)
    #res2 = comm.recv(source=2, tag=2+offset)
    #for i in range(1, slice):
    #    c = comm.recv(source=2, tag=2+i+offset)
    #    res2 = np.vstack((res2, c))

    #print ("receiving response 3")
    #offset3 = comm.recv(source=3, tag=3)
    #res3 = comm.recv(source=3, tag=3+offset)
    #for i in range(1, slice):
    #    c = comm.recv(source=3, tag=3+i+offset)
    #    res3 = np.vstack((res3, c))        
    print ("checking response")
    res1 = np.zeros(shape=(slice, numberColumns))
    comm.Recv([res1, MPI.FLOAT], source=1, tag=1)
    res2= np.zeros(shape=(slice, numberColumns))
    comm.Recv([res2, MPI.FLOAT], source=2, tag=2)
    res3 = np.zeros(shape=(slice, numberColumns))
    comm.Recv([res3, MPI.FLOAT], source=3, tag=3)
    
    kl = np.vstack((res1, res2, res3))
    print ("Result AxB")
    print (kl)   

comm.Barrier()
##if rank == 1:
##    recv_data = comm.recv(source=0, tag=1)
##    b = comm.recv(source=0, tag=4)    
##    print  rank, recv_data
##    print " "
##    print b
##    print " "
##
##if rank == 2:
##    recv_data = comm.recv(source=0, tag=2)
##    b = comm.recv(source=0, tag=5)      
##    print  rank, recv_data
##    print " "
##    print b
##    print " "
##
##if rank == 3:
##    recv_data = comm.recv(source=0, tag=3)
##    b = comm.recv(source=0, tag=6)      
##    print  rank, recv_data
##    print " "
##    print b
##    print " "


#comm.Bcast(a, root=0)
#comm.Bcast(b, root=0)




    #comm.Gather(sendbuf=None, recvbuf=a, root=TaskMaster)
    #comm.Gather(sendbuf=None, recvbuf=b, root=TaskMaster)
#sys.stdout.write("Process %d printing.\n" % (rank))
#for r in a:
#    np.savetxt(sys.stdout, r, fmt='%.4f')
        #print r
      #sys.stdout.write("Process %d printing value %d.\n" % (rank, r))


