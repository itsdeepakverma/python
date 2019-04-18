se# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:07:23 2019

@author: Admin
"""

import pandas as pd


df=pd.read_csv("D:\\Python\\DataSet\\training_titanic.csv")

df.isnull().any(axis=0)

df[df.isnull().any(axis=1)]

df_nw=df.dropna()

df_fill=df.fillna(df.mean())

df_fill['Child']=df_fill['Age'].apply(lambda x:1 if x<18 else 0)

child_sur=df_fill['Child'].value_counts(normalize=True)

print("No of % older Survived is={} and NO of % child Survived is= {}".format(child_sur[0]*100,child_sur[1]*100))