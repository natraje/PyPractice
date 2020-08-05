'''
Created on Dec 22, 2019

@author: natra
'''
import pandas as pd
import numpy as np
df=pd.read_csv('C://NAT//ML & AI//testfiles/forestfires.csv')
print(df.head())
print('------------')
print(df[1:3])
print(df[1::3]) ##Alternate
print('------------')
print(df['month'])
print('------------')
print(df.shape)
print('------------')
dfnew=df[['month','day','temp']]
#Position based indexing using df.iloc
#Label based indexing using df.loc
print(df.iloc[:,:])
print(df.iloc[[2,3,5],3:4])
print('------------')
print(df.loc[:,:])
## get details with march temp 
print(df.loc[(df.month=='mar')])
print('------------')
print(df.loc[(df.month=='mar'),['temp','wind']])