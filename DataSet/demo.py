# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 10:49:10 2018

@author: Admin
"""
#name=input("enter name")

"""import math as mt

print (mt.sqrt(16))

from math import sqrt

print(sqrt(4))"""

import pandas as pd

dataset=pd.read_csv('Income_Data.csv')

#extracting feature and lables from dataset
features=dataset.iloc[:,:-1].values

labels=dataset.iloc[:,-1].values

from sklearn.linear_model_selection import train_test_split



from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
