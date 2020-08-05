'''
Created on Jan 26, 2020

@author: natra
'''
import pandas as pd
import numpy as np

rating=pd.read_csv('C://NAT//ML & AI//testfiles/Data Sourcing/rating_final.csv')
#Remove Duplicate rows
rating_update = rating.drop_duplicates()

print(rating.shape)
print(rating_update)