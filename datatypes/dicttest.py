'''
Created on Dec 19, 2019

@author: natra
'''

dict1={'t1':1,'t2':2}
print(dict1)
print(dict1.values())
dict1['t3']=3
print(dict1)
for k,v in dict1.items():
    print(k,v)

d = {0: 'Fish', 1: 'Bird', 2: 'Mammal'}
for i in d:
    print(i)

d = {0, 1, 2}
for x in d:
    print(d.add(x))

help(dict)