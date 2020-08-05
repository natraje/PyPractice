'''
Created on Jan 26, 2020

@author: natra
'''
import pandas as pd
import numpy as np

customer=pd.read_csv('C://NAT//ML & AI//testfiles/Data Sourcing/cust_dimen.csv')
#Substr or extract
customer['Cust_id'] =customer.Cust_id.str.slice(5) 
#customer.Cust_id.str.extract('Cust_', expand=True)
print(customer.head(10))