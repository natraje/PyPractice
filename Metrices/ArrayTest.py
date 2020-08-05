'''
Created on Dec 26, 2019

@author: natra
'''
import numpy as np
A = np.array([[1, 2], 
             [2, 0]])

print(A.shape) # shape
print(A[:, 0]) # first column
print(A[1, :]) # second row

##Transpose
A1 = np.array([[1, 3],[2, 0]])
print(A1.T)

#Inverse
A2 = np.array([[2, 1, -1], 
              [1, 0, -1], 
              [-2, 0, 1]])

print(np.linalg.inv(A2))