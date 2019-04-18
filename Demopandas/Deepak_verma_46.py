# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:06:48 2019

@author: Admin
"""

import pandas as pd


df=pd.read_csv("D:\\python\\\\Dataset\\Loan.csv")

feature=df.iloc[:,:-1].values
label=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
f_train,f_test,l_train,l_test=train_test_split(feature,label,test_size=0.2,random_state=0)

list=[0,1,2,3,4,5,11]

for x in list:
    labelencoder=LabelEncoder()
    feature[:,x]=labelencoder.fit_transform(feature[:,x])

onehotencoder=OneHotEncoder(categorical_features=[11])
feature=onehotencoder.fit_transform(feature).toarray()


labelencoder1=LabelEncoder()
label=labelencoder1.fit_transform(label)