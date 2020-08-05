'''
Created on Dec 26, 2019

@author: natra
'''
# determinant
import numpy as np
A = np.array([[2, 3], [-1, 4] ])
x=np.linalg.det(A)
print(x)
A = np.array([[1,3], [2,6] ])
x=np.linalg.matrix_rank(A)
print(x)

# system of three equations
A = np.array([[1, 5, -1], 
              [2, 3, -2], 
              [-3, 4, 0]])
b = np.array([1, 2, 0])

# compute the inverse
A_inv = np.linalg.inv(A)

# solution: A_inv * b
x = np.dot(A_inv, b)
print(x) # returns [ 0.  0. -1.]


A = np.array([[2, -1, -1], 
              [2, -1, 1], 
              [4, -2, -3]])

b = np.array([1, 0, -1])

# compute the inverse
A_inv = np.linalg.inv(A)

# solution: A_inv * b
x = np.dot(A_inv, b)
print(x) # returns [ 0.  0. -1.]
