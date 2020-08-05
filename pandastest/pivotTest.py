'''
Created on Dec 23, 2019

@author: natra
'''
import  pandas as pd
df=pd.read_csv('C://NAT//ML & AI//testfiles/forestfires.csv')
pt=df.pivot_table(values='wind', index='month', aggfunc='mean')
print(pt)

print(df.pivot_table(values='wind', index='month', aggfunc='min'))
#Group the data 'df' by 'month' and 'day' and find the mean value for column 'rain' and 'wind' using the pivot table command.
df_1 = df.pivot_table(values=['rain','wind'] ,index=['month','day'],aggfunc='mean')
print(df_1.head(20))