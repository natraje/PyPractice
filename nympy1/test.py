import numpy as np
l1=[1,2,3,4,5]
l2=[1,2,3,4,5]

#convert list to NP array
npar1=np.array([l1,l2])
print('NP array',npar1)
npar2=np.array([l1,l2])
np_add=npar1+npar2
print('Add',np_add)
np_mul=npar1*npar2
print('Mul',np_mul)
np_sq=npar1**2
print('SQ:',np_sq)

np_o=np.ones((2,2),dtype = int)
print('Ones:',np_o)
#Shape
print("Shape:",np_o.shape)
print("Dim:",np_o.ndim)

#reshape
rar=np.arange(24).reshape(2,3,4)
print("reshape:",rar)

#newar=np.random.random(10)
newar=np.arange(10)
print(newar)
print(newar[5])
print(newar[[5,4,6]])

#Get all elements from given slot
print("Get from nth Element:",newar[3:])
#Get first x element
print("Get first n element:",newar[:4])
#Get from 1 to i+n
print("Get first n element:",newar[2:4])
print("Get skipped element:",newar[0::2]) 
print("Get skipped element:",newar[2::3])

## Vectorize the function
a=np.arange(20).reshape(4,5)
print(a)
fn=np.vectorize(lambda x:x**2)
print(fn(a))