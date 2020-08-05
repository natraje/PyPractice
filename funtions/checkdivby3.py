'''
Created on Dec 20, 2019

@author: natra
'''
mylist=[3,4,5,6,7,90,21]
divby3=lambda x: x%3==0
lt1=list(filter(divby3,mylist))
print(lt1)
print( ((500//7) % 5) ** 3)

L = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
print(L[2: ])