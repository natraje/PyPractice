'''
Created on Dec 22, 2019

@author: natra
'''
import pandas as pd
df=pd.read_csv('C://NAT//ML & AI//testfiles/forestfires.csv')
df1=df.loc[1:3,['month','wind']]
print(df1)
df2=df.loc[5:15,['month','wind']]
print('-------------------\n',df2)
dfmerge=pd.merge(df1,df2,how='inner',on='wind')
print('-------------------\n Merge \n-------------------\n',dfmerge)