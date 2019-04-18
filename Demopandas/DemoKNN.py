# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:48:54 2019

@author: Admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import data set

data=pd.read_csv("D:\\python\\dataset\\Social_Network_Ads.csv")

feature=data.iloc[:,2:-1].values
lable=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split

ftrain,ftest,ltrain,ltest=train_test_split(feature,lable,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler

ss=StandardScaler()
ftrain=ss.fit_transform(ftrain)
ftest=ss.transform(ftest)

#fitting KNN model on data

from sklearn.neighbors import KNeighborsClassifier

classifier=KNeighborsClassifier(n_neighbors=5,p=2)

classifier.fit(ftrain,ltrain)

#making prediction

pred=classifier.predict(ftest)

#confusion Matrix
from sklearn.metrics import confusion_matrix

cm=confusion_matrix(ltest,pred)