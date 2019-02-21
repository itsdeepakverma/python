# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:07:34 2019

@author: Admin
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("D:\\Python\\DataSet\\Automobile.csv")

values=df['make'].value_counts()
label=df['make'].value_counts().index.values

a=values.head(10).values

b=label.tolist()

bb=b[:10]


plt.pie(a,labels=bb,autopct='%.2f')