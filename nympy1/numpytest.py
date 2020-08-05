'''
Created on Dec 26, 2019

@author: natra
'''
import numpy as np
rar=np.arange(132).reshape(11,12)
print(rar[:,:3])


ar=[[1,2,3],[44,5,6]]
print(rar)
n=8
c = np.ones((n,n), dtype = 'int')
for i in range(1,n-1):
    for j in range(1,n-1):
        c[i,j]=0
c1 = np.ones((n,n), dtype = 'int')
c1[1:-1, 1:-1] = 0
print(c1)