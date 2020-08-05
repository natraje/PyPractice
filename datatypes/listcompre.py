'''
Created on Dec 18, 2019

@author: natra
'''
lst=[x**2 for x in range(10)]
print(lst)
## Nested if with a single line of code
arr1=[(x,y) for x in [1,2,3] for y in[2,4,3] if x!=y]
print(arr1)