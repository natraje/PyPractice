'''
Created on Jan 27, 2020

@author: natra
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('C://NAT//ML & AI//testfiles/Data Sourcing/EDA_Gold_Silver_prices.csv')
#Remove Duplicate rows

## column count and row count
print(len(df))
print(df.columns)
#Index(['Month', 'SilverPrice', 'GoldPrice'], dtype='object')
##Correlation 
print(df.corr(method ='pearson') )
## filter 2008 data
df1=pd.read_csv('C://NAT//ML & AI//testfiles/Data Sourcing/EDA_Gold_Silver_prices1.csv')
print(df1.corr(method ='pearson') )

df2=pd.read_csv('C://NAT//ML & AI//testfiles/Data Sourcing/currencies.csv')
print(df2.columns)
print(df2.corr())
corr = df2.corr()
corr.style.background_gradient(cmap='coolwarm')
plt.matshow(corr)
plt.show()