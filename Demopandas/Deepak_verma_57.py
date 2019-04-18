# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 12:04:10 2019

@author: Admin
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import confusion_matrix
data=pd.read_csv("D:\\python\\dataset\\affairs.csv")

feature=data.iloc[:,:-1].values
label=data.iloc[:,-1].values

OHE=OneHotEncoder(categorical_features=[6,7])

feature=OHE.fit_transform(feature).toarray()

ftrain,ftest,ltrain,ltest=tts(feature,label,test_size=0.2,random_state=0)

lr=LogisticRegression(random_state=0)

lr.fit(ftrain,ltrain)

predictlabel=lr.predict(ftest)

cm=confusion_matrix(ltest,predictlabel)