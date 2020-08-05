'''
Created on Dec 19, 2019

@author: natra
'''
def func1():
    print('test')
    print('2test')   
func1()


def say(message, times = 1):
    print(message * times)

say('Hello')
say('World', 5)

min = (lambda x, y: x if x < y else y)
print(min(101*99, 102*98))

input_list = ['sds','sads','fdfg']
xt=lambda x: 1 if x.upper().startswith('S') else 0
cube=sum(map(xt,input_list))
print(cube)