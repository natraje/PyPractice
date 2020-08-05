import pandas as pd
import numpy as np

marks=pd.read_csv('C://NAT//ML & AI//testfiles/Data Sourcing/class-grades.csv')

## Sum of missing values column wise
print('Column wise missing values:', marks.isnull().sum())
print('----------------------------')
print('row wise missing value',marks.isnull().all(axis=1).sum())
print('Missing row values at column wise',marks.isnull().sum(axis=1))
print(marks[(marks.isnull().sum(axis=1))<5])