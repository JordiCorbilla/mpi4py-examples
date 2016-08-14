# mpi4py-examples

This repository contains advanced parallel computing scripts to run against an MPI cluster.

**License:** GNU General Public License.

The creation and configuration of the cluster can be seen here:

- [Creating a Raspberry Pi 3 cluster for parallel computing](http://thundaxsoftware.blogspot.co.uk/2016/07/creating-raspberry-pi-3-cluster.html)
- [Raspberry Pi 3 Cluster test](http://thundaxsoftware.blogspot.co.uk/2016/08/raspberry-pi-3-cluster-test.html)
 
The example provided in this repository is about matrix multiplication via MPI. The approach used is by slicing the matrix and sending each chunk to a particular node of the cluster, perform the calculations and send the results back to the main node.

The results of the execution can be seen below (time in seconds):

Test | Sequential Time | CPU1 | CPU2 | CPU3 | CPU4 | CPU1 | CPU2 | CPU3 | CPU4 | CPU1 | CPU2 | CPU3 | CPU4 | Max | Speedup
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
12x12 | 0.01111 | 0.00525 |  |  |  | 0.0037 |  |  |  | 0.0037 |  |  |  | 0.00525 | 2.116190476
12x12 | 0.01111 | 0.00292 | 0.00202 |  |  | 0.00208 | 0.00303 |  |  | 0.00206 | 0.00211 |  |  | 0.00303 | 3.666666667
12x12 | 0.01111 | 0.00197 | 0.00175 | 0.00129 |  | 0.00205 | 0.00182 | 0.00122 |  | 0.00218 | 0.00183 | 0.00127 |  | 0.00218 | 5.096330275
12x12 | 0.01111 | 0.00214 | 0.00233 | 0.00212 | 0.00194 | 0.00202 | 0.00234 | 0.00267 | 0.00185 | 0.00201 | 0.00222 | 0.00209 | 0.00241 | 0.00267 | 4.161048689
60x60 | 1.29955 | 0.4778 |  |  |  | 0.36717 |  |  |  | 0.36728 |  |  |  | 0.4778 | 2.719861867
60x60 | 1.29955 | 0.35127 | 0.27552 |  |  | 0.20697 | 0.34767 |  |  | 0.27474 | 0.207 |  |  | 0.35127 | 3.699575825
60x60 | 1.29955 | 0.21966 | 0.22068 | 0.15385 |  | 0.22046 | 0.22196 | 0.15476 |  | 0.22054 | 0.22058 | 0.15436 |  | 0.22196 | 5.854883763
60x60 | 1.29955 | 0.18464 | 0.18589 | 0.18397 | 0.18379 | 0.18283 | 0.1851 | 0.18473 | 0.18374 | 0.18373 | 0.18427 | 0.18396 | 0.18381 | 0.18589 | 6.990962397
144x144 | 15.02287 | 5.08906 |  |  |  | 4.99491 |  |  |  | 4.93309 |  |  |  | 5.08906 | 2.951993099
144x144 | 15.02287 | 2.78648 | 2.90336 |  |  | 2.67886 | 2.78634 |  |  | 2.89459 | 2.68409 |  |  | 2.90336 | 5.174304943
144x144 | 15.02287 | 3.11941 | 2.69587 | 2.022 |  | 3.12694 | 2.69165 | 2.0254 |  | 3.12809 | 2.68855 | 2.01999 |  | 3.12809 | 4.802569619
144x144 | 15.02287 | 2.37735 | 2.3879 | 2.2758 | 2.38267 | 2.37713 | 2.27037 | 2.38764 | 2.37814 | 2.25782 | 2.38018 | 2.38604 | 2.27187 | 2.3879 | 6.29124754
216x216 | 51.69995 | 17.26683 |  |  |  | 17.08989 |  |  |  | 16.66551 |  |  |  | 17.26683 | 2.994177275
216x216 | 51.69995 | 9.67602 | 8.63827 |  |  | 8.60859 | 9.65453 |  |  | 8.62195 | 8.62782 |  |  | 9.67602 | 5.343100779
216x216 | 51.69995 | 10.52823 | 9.46254 | 7.30951 |  | 10.51718 | 9.44692 | 7.30529 |  | 10.54083 | 9.48649 | 7.28061 |  | 10.54083 | 4.90473236
216x216 | 51.69995 | 8.13615 | 8.12379 | 8.00465 | 8.13003 | 8.13992 | 7.94381 | 8.14352 | 8.1071 | 8.00023 | 8.13681 | 8.14298 | 7.999 | 8.14352 | 6.348599868

![](https://2.bp.blogspot.com/-wsD4xAfhIFk/V6-1lIva0wI/AAAAAAAAFp0/PnwvU9qbMJgGvmNXLseKwMYXRq-hl4CSwCLcB/s640/alltogether.png)
![](https://3.bp.blogspot.com/-PBgNpQZDm50/V6-0MGQiqDI/AAAAAAAAFpo/phdbxb8zlogdMtCJigMKANqYYnSxuko_gCLcB/s640/speedup.png)

**Licence**
-------

    mpi4py-examples Copyright (C) 2016 Jordi Corbilla

    This program is free software: you can redistribute it and/or modify it under the terms of the GNU 
    General Public License as published by the Free Software Foundation, either version 3 of the License,
    or (at your option) any later version.
    
    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even 
    the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public
    License for more details.
    
    You should have received a copy of the GNU General Public License along with this program. 
    If not, see http://www.gnu.org/licenses/.

## Sponsors
No sponsors yet! Will you be the first?

[![PayPayl donate button](https://img.shields.io/badge/paypal-donate-yellow.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=L5FCF6LX5C9AW "Donate once-off to this project using Paypal")
