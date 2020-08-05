'''
Created on Dec 23, 2019

@author: natra
'''
import pandas as pd
r1=pd.read_csv('C://NAT//ML & AI//testfiles/restaurant-1.csv')
r2=pd.read_csv('C://NAT//ML & AI//testfiles/restaurant-2.csv')

print('-------------------\n Merge \n-------------------\n')
r3=pd.concat([r1,r2],axis=0,sort=False)
print(r3)


# Defining the three dataframes indicating the gold, silver, and bronze medal counts
# of different countries
gold = pd.DataFrame({'Country': ['USA', 'France', 'Russia'],
                         'Medals': [15, 13, 9]}
                    )
silver = pd.DataFrame({'Country': ['USA', 'Germany', 'Russia'],
                        'Medals': [29, 20, 16]}
                    )
bronze = pd.DataFrame({'Country': ['France', 'USA', 'UK'],
                        'Medals': [40, 28, 27]}
                    )

gold.set_index('Country',inplace=True)
silver.set_index('Country',inplace=True)
bronze.set_index('Country',inplace=True)
medals=gold.add(silver,axis=0,fill_value=0).add(bronze,axis=0,fill_value=0).sort_values(by=['Medals'],ascending=False )
print(medals)
