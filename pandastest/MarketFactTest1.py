'''
Created on Dec 26, 2019

@author: natra
'''
import pandas as pd
import numpy as np

df=pd.read_csv('C://NAT//ML & AI//testfiles/melbourne.csv')
## Sum of missing values column wise

missingValues=round(100*(df.isnull().sum()/len(df.index)),2) ## What % values is null in each column
s1=df.isnull().sum() 
cols=[]
percent=[]
rCols=[]
for i,j in missingValues.items():
    if j>30:
        rCols.append(i)
    cols.append(i)
    percent.append(j)

dfPercent=pd.DataFrame({ 'Columns': cols, 'Percent': percent } )
dfPercent.set_index('Columns', inplace=True)
print(dfPercent)
dfPercent.sort_values(by='Percent',ascending=False, inplace=True)
print(rCols)

## Drop the columsn with more than 30%
df1=df.drop(rCols,axis=1)
missingValues=round(100*(df1.isnull().sum()/len(df1)),2)
print(missingValues)
## On DF1 operate on row with 5 or more nulls
df2=df1[df1.isnull().sum(axis=1)<5]
missingValues2=round(100*(df2.isnull().sum()/len(df2)),2)
print(missingValues2)
df3=df2[-np.isnan(df['Price'])]
missingValues3=round(100*(df3.isnull().sum()/len(df3)),2)
print(missingValues3)


#print('How many rows have Missing Values:',df.isnull().sum())
#print('-------------------------------------',df1.head())

