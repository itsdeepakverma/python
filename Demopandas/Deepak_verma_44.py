# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:16:52 2019

@author: Admin
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("D:\\python\\DataSet\\Cars.csv")

feature=dataset.iloc[:,1:]
label=dataset.iloc[:,0]

from sklearn.model_selection import train_test_split

feature_train,feature_test,label_train,label_test=\
train_test_split(feature,label,test_size=0.5,random_state=0)

feature_train.to_csv("feature_train.csv")
feature_test.to_csv("feature_test.csv")
label_train.to_csv("label_train.csv")
label_test.to_csv("label_test.csv")