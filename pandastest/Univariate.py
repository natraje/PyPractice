'''
Created on Jan 26, 2020

@author: natra
'''
import pandas as pd
import numpy as np

df=pd.read_csv('C://NAT//ML & AI//testfiles/Data Sourcing/popularity (1).csv')
#Remove Duplicate rows

## column count and row count
print(len(df))
print(df.columns)
print(df[' shares'])
q = df[" shares"].quantile(0.99)
print(q)
q_low = df[" shares"].quantile(0.01)
print(q_low)

q_hi  = df[" shares"].quantile(0.75)
print(q_hi)
df_filtered = df[(df[" shares"] < q_hi) & (df[" shares"] > q_low)]
#print(df_filtered[" shares"].mean())

df1=df[df[' shares']<10801]
print(df1.describe())

print((len(df)-len(df1))/len(df))