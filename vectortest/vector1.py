'''
Created on Dec 23, 2019

@author: natra
'''
import math
import numpy as np
pi = math.pi
deg=np.arccos(3/(np.sqrt(5)*np.sqrt(2)))*(180/pi)
print(deg)

a1=[2,1,0,0]
a2=[0,0,1,1]
a3=[1,1,0,0]
a4=[1,1,1,0]
print(np.arccos(3/(np.sqrt(5)*np.sqrt(2)))*(180/pi)) #1,3
print(np.arccos(3/(np.sqrt(5)*np.sqrt(3)))*(180/pi)) #1.4
print(np.arccos(2/(np.sqrt(2)*np.sqrt(3)))*(180/pi)) #3,4