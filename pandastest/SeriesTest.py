'''
Created on Dec 22, 2019

@author: natra
'''
import numpy as np
import pandas as pd
s=pd.Series([1,2,3,4,5])
s.apply(lambda x: x**2) # Apply funciton can be applied only on series not on arrays

fn=lambda x: x*2
ar=(np.array(range(1,11))**2)
print(ar)

s1=pd.Series(ar,range(1,11))
print(len(s1))
for i,j in s1.items():
    print('test',i,j)
