'''
Created on Jan 27, 2020

@author: natra
'''
import pandas as pd
import numpy as np

df=pd.read_excel('C://NAT//ML & AI//testfiles/Data Sourcing/EDA_census.xlsx')
#Remove Duplicate rows

## column count and row count
print(len(df))
print(df.columns)
df1=pd.read_excel('C://NAT//ML & AI//testfiles/Data Sourcing/femalelit.xlsx')
print(df1.columns)
print(df1.groupby(['State']).sum())