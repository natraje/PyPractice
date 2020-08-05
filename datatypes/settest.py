'''
Created on Dec 18, 2019

@author: natra
'''

setTest={'test',"t2"}
print(setTest)
print('t2' in setTest)

set1=set("abcdeftg")
set2=set('dfyhjuy')
print(set1-set2)
print(set1|set2)
print(set1&set2)
print(set1^set2)

s={x for x in 'abcrdabceabf' if x not in 'abc'}
print (s)


C = set([2, 5, 9, 12, 13, 15, 16, 17, 18, 19]) #cricker
F = set( [2, 4, 5, 6, 7, 9, 13, 16]) #football
H = set([1, 2, 5, 9, 10, 11, 12, 13, 15]) #hockey
  
al=C.union(F,H)
threeonly=C.intersection(F,H)
threeonlyList=sorted(list(threeonly))
print(threeonlyList)
cr_ftonly=C.intersection(F).difference(H)
cr_ftonlylist=sorted(list(cr_ftonly))
print(cr_ftonlylist)
twoonly1=(C.intersection(F).difference(H)).union(C.intersection(H).difference(F),F.intersection(H).difference(C))
twoonly1List=sorted(list(twoonly1))
print(twoonly1List)
notinAny=sorted(list(set(range(1,21)).difference(al)))
print(notinAny)

    