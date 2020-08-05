'''
Created on Dec 25, 2019

@author: natra
'''

class Car(object):
    name=''
     

    def __init__(self, params):
        '''
        Constructor
        '''
    def drive(self):
        print('Driving')

corolla= Car('');
print(corolla.drive())    

class AddTest():    
    def addNums(self,num1,num2):
        self.num1=num1+1
        self.num2=num2+1
        
    def printSum(self):
        print('N1:',self.num1)
        print('N2:',self.num2)

test=AddTest()
test.addNums(5, 6)
print(test.printSum())