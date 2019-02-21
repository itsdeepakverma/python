# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:48:21 2019

@author: Admin
"""

import pandas as pd

df=pd.read_csv("D:\\Python\\DataSet\\Salaries.csv")

df.head()

df.tail()

df.dtypes

df.columns

df.axes

df.ndim

df.size

df.shape

df.values

df.describe()

df.max

df.min()

df.mean()

df.head(50).mean()

df['rank']
df['salary'].mean()

df['salary'].describe()

df['salary'].count()

df_rank=df.groupby(['rank'])

type(df_rank)


df_rank.mean()

type(df.groupby('rank')[['salary']].mean())
df.groupby(['rank'],sort=False)[['salary']].mean()

df_sub=df[df['salary']>120000]
print(df_sub)

a=df[['rank','salary']]

df.loc[10:20,['rank','salary']]

df.iloc[1,[0,1]]

df.iloc[1:,0:]

df_sorted=df.sort_values(by='salary')
print(df_sorted)

df_sorted=df.sort_values(by=['salary','service'],ascending=[True,False])

df_sorted.head()

df[df.isnull().any(axis=1)]

df.dropna()


df_new_col=df.assign(mean=df['salary'].mean())


a=input("enter number")
b=int(a,8)
print(b)

