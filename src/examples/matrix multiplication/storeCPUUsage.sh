#!/bin/bash
# @Author: Jordi Corbilla
while true; do 
  (echo "%CPU %MEM ARGS $(date)" && ps -e -o pcpu,pmem,args --sort=pcpu | cut -d" " -f1-5 | tail) >> cpu.log; sleep 0.1; 
done

#Example results;
#%CPU %MEM ARGS Fri 12 Aug 19:11:20 UTC 2016
#87.0  1.8 python /home/pi/mpi4py-2.0.0/demo/matrixmultiplication.py
#90.0  1.8 python /home/pi/mpi4py-2.0.0/demo/matrixmultiplication.py
#90.5  1.9 python /home/pi/mpi4py-2.0.0/demo/matrixmultiplication.py
#92.5  1.8 python /home/pi/mpi4py-2.0.0/demo/matrixmultiplication.py