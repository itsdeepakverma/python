# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:54:25 2019

@author: Admin
"""

import pandas as pd

df=pd.read_csv("D:\\python\\dataset\\Loan.csv")

C_df=df.select_dtypes(include='object')

df.isnull().any(axis=0)

#for label encoding
for x in df.columns:
    df[x]=df[x].astype('category')
    df[x]=df[x].cat.codes


#for OneHotEncoding
    
    
#df=pd.get_dummies(df,columns=['Gender'],prefix=['G'])
C_df=pd.get_dummies(C_df,columns=['Gender','Married','Dependents','Education',\
            'Self_Employed','Property_Area'],prefix=['G','M','D','E','SE','PA'])
    
    
  list=[]
  