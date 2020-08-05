'''
Created on Jan 27, 2020

@author: natra
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('C://NAT//ML & AI//testfiles/Data Sourcing/nas.csv')
print(len(df))
print(df.columns)
df.corr()