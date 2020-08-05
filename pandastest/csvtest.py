'''
Created on Dec 22, 2019

@author: natra
'''
import pandas as pd
df=pd.read_csv('aba.csv')
#print(df.columns)
print(df.head())
#print(df.tail())
#print(df.info())
#print(df.describe())
df.set_index('ABA', inplace=True)
print('Index is changed')
print(df.head())
#df.sort_index(axis=0,ascending=False)
df.sort_values(by='NAME',ascending=False)
print('Sorting is changed')
print(df.head())

print('--------------------')
dfnew=pd.read_csv('C://NAT//ML & AI//testfiles/forestfires.csv')
dfnew2=dfnew.set_index('X',inplace=False)
print(dfnew2.head())