'''
Created on Dec 26, 2019

@author: natra
'''
import pandas as pd
import numpy as np
class MarketFactAnalysis():
    df=pd.read_csv('C://NAT//ML & AI//testfiles/melbourne.csv')
    #

    def calculateAlgo(self):
        df1=self.df;
        roundOff=self._findPercent(df1,0)
        print(roundOff)
        remCols=self._analyzerouding(roundOff,30)
        print(remCols)
        df1=df1.drop(remCols,axis=1)
        ## Get rid off rows having more than 5 null columns
        df1=df1[df1.isnull().sum(axis=1)<6]
        roundOff2=self._findPercent(df1,0)
        print(roundOff2)
        df1=df1[-np.isnan(df1['Price'])]
        roundOff3=self._findPercent(df1,0)
        print(roundOff3)
        #Analyze landsize
        s1=df1['Landsize'].describe()
        df1=df1[-np.isnan(df1['Landsize'])]
        roundOff4=self._findPercent(df1,0)
        print(roundOff4)
        print(df1.loc[:,['Lattitude','Longtitude']].describe())
        df1.loc[np.isnan(df1['Lattitude']),['Lattitude']]=df1['Lattitude'].mean()
        df1.loc[np.isnan(df1['Longtitude']),['Longtitude']]=df1['Longtitude'].mean()
        roundOff5=self._findPercent(df1,0)
        print(roundOff5)    
        print(df1.loc[:,['Car','Bathroom']].describe())
        ## find the spread of car park by category
        df1['Car']=df1['Car'].astype('category')
        print(df1['Car'].value_counts()) 
        ## impute car park 0 as 2Ca
        df1.loc[pd.isnull(df1['Car']),['Car']]=2
        df1['Bathroom']=df1['Bathroom'].astype('category')
        df1.loc[pd.isnull(df1['Bathroom']),['Bathroom']]=1
        print(df1.shape)
    @staticmethod
    def _findPercent(dfTemp,axisVal):
        return round(100*(dfTemp.isnull().sum(axis=axisVal)/len(dfTemp.index)),2)

    @staticmethod
    def _analyzerouding(roundOff,threshold):
        rCols=[]
        for i,j in roundOff.items():
            if j>=threshold:
                rCols.append(i)
        return rCols;       
    
    
NFA=MarketFactAnalysis();
NFA.calculateAlgo();
        
     