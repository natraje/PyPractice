'''
Created on Dec 19, 2019

@author: natra
'''

score=int(input("Enter your score:"))
destinction=90
passscore=40
super=75
sups="bsfsdg"
if sups.startswith('a') or sups.startswith('b'):
    print(" YES ")
if score >= destinction:
   print(" Great score ")
elif score >= super:
   print(" Superb ")
elif score >= passscore:
   print(" just saved ")  
else:
   print(" take again") 
if True or True:
    if False and True or False:
        print('A')
    elif False and False or True and True:
        print('B')
    else:
        print('C')
else:
    print('D')