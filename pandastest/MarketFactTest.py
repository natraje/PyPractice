'''
Created on Dec 26, 2019

@author: natra
'''
import pandas as pd
import numpy as np

df=pd.read_csv('C://NAT//ML & AI//testfiles/melbourne.csv')
df=pd.read_csv('C://NAT//ML & AI//testfiles/melbourne.csv')
## Sum of missing values column wise
print('Details:', df.isnull().sum())
missingValues=round(100*(df.isnull().sum()/len(df.index)),2) ## What % values is null in each column
print('testnat')
print('-------------------------------------')
print('How many rows have Missing Values:',df.isnull().all(axis=1).sum())
print('-------------------------------------')
print('How many rows atleast have Missing Values at columns:',df.isnull().sum(axis=1))
print('-------------------------------------')
print('Missing Values Column Wise:',missingValues)
# Remove columns having more than 30% misssing values
#BuildingArea     57.46 YearBuilt        50.99 CouncilArea      33.51
df=df.drop(['BuildingArea','YearBuilt','CouncilArea'],axis=1)
missingValues1=round(100*(df.isnull().sum()/len(df.index)),2)
print('-------------------------------------')
print('Missing Values Column Wise:',missingValues1)
## Find the rows which has more than 5 columns null values
print('-------------------------------------')
print(df[(df.isnull().sum(axis=1))>5])
print(df[(df.isnull().sum(axis=1))>5].index)
print('-------------------------------------')
# Remove NAN rows in price columns
df=df[-np.isnan(df['Price'])]
missingValues2=round(100*(df.isnull().sum()/len(df.index)),2)
print('-------------------------------------')
print('Missing Values Row Wise:',missingValues2)

