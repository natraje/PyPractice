'''
Created on Dec 18, 2019

@author: natra
'''
matrix=[[1,2,3],[4,5,6],[7,8,9]]
trans=[[row[i] for row in matrix] for i in range(3)]
print(trans)