# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:26:44 2019

@author: Admin
"""

import pandas as pd
import numpy as np

df=pd.read_csv("D:\\Python\\DataSet\\Automobile.csv")

df[df.isnull().any(axis=1)]

df_fill=df.fillna(df.mean())
df_fill.isnull().any(axis=0)

nparray=np.asarray(df_fill['price'])

print("minimum price={}".format(nparray.min()))

print("minimum price={}".format(nparray.max()))

print("minimum price={}".format(nparray.mean()))

print("minimum price={}".format(nparray.std()))

