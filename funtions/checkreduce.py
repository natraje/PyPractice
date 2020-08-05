'''
Created on Dec 20, 2019

@author: natra
'''
red=reduce(lambda x,y: x+y, range(1,5))

print(red)

lt=[1,2,3,4,5,6,7,8]
red1=reduce(lambda x,y: x+y, lt)

    
    import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)red1)