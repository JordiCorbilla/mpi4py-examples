#!/usr/bin/env python

"""
@Author: Jordi Corbilla
@Description: Numpy test script

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

import numpy as np
from random import randint

numberRows = 3
numberColumns = 3

a = np.zeros(shape=(numberRows, numberColumns))
res = np.zeros(shape=(numberColumns))
def populateMatrix( p ):
    for i in range(0, numberRows):
        for j in range(0, numberColumns):
            p[i][j] = (i+1)*(j+1) #i+j * randint(0,9)

populateMatrix(a)
print ("All a")
print(a)
print ("column b")
b = a[:,0]
print (b)
print ("column c")
c = a[:,1]
print (c)
print ("column d")
d = a[:,2]
print (d)
print ("row e")
e = a[0,:]
print (e)
print ("exb")
val = 0.0

ai = 0
for k in range(0, numberColumns):
    q = a[:,k] #get the column we want
    print ("colum ")
    print (e)
    print (q)
    #print (res[ai])
    for x in range(0, numberColumns):
        print(e[x])
        #for y in q:
        #    print(y)
        res[ai] = res[ai] + (e[x]*q[x])
    print (res[ai])
    ai = ai + 1

print (res)

w = np.array([.5, .4, .3])
kl = np.vstack((w, res, res))
print (kl)

print ("")
print ("z")
z = np.array([[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]])
print (z)

s = np.array([1, 2, 3])
print (s)
print (z.dot(s))
print (s * z)


a = np.array([[1,2,3,4,5,6],[3,4,5,4,5,6],[4,5,6,4,5,6],[1,2,3,4,5,6],[3,4,5,4,5,6],[4,5,6,4,5,6]])
print (a)
print (a[0,:])

b = a[0,:]
b = np.vstack((b, a[1,:]))
b = np.vstack((b, a[2,:]))
b = np.vstack((b, a[3,:]))
print (b)






