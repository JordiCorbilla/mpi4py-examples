#!/bin/bash
# @Author: Jordi Corbilla
# @Description: Parallel MPI Matrix Multiplication (NxN)
for STEPS in 12 60 144 216; do
	for TEST in 1 2 3 4 5 6 7 8 9 10; do
		mpiexec -f machinefile -n 2 python /home/pi/mpi4py-2.0.0/demo/matrixmultiplication.py $STEPS $STEPS >> mpi$STEPS.log
	done
done
