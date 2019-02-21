# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:52:55 2019

@author: Admin
"""

# number of survived and dead
import pandas as pd


df=pd.read_csv("D:\\Python\\DataSet\\training_titanic.csv")

df.isnull().any(axis=0)

df[df.isnull().any(axis=1)]

df_nw=df.dropna()

df_fill=df.fillna(df.mean())

df_fill.isnull().any(axis=0)


a=df_fill['Survived'].value_counts()
print("No of person Survived is={} and NO of person Dead is= {}".format(a[0],a[1]))

b=df_fill['Survived'].value_counts(normalize=True)
print("No of % person Survived is={} and NO of % person Dead is= {}".format(b[0]*100,b[1]*100))


df_fill['Sex'].value_counts()

male_sur=df_fill[df_fill['Sex']=='male']['Survived'].value_counts(normalize=True)
print("No of % male Survived is={} and NO of % male Dead is= {}".format(male_sur[0]*100,male_sur[1]*100))
female_sur=df_fill[df_fill['Sex']=='female']['Survived'].value_counts(normalize=True)
print("No of % female Survived is={} and NO of % female Dead is= {}".format(female_sur[0]*100,female_sur[1]*100))
