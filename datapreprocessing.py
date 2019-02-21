# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 17:09:03 2019

@author: Admin
"""

import pandas as pd

df = pd.read_csv("Data.csv")

features = df.iloc[:,:-1].values
labels = df.iloc[:,-1].values

from sklearn.preprocessing import Imputer

imp = Imputer()
features[:,1:3] = imp.fit_transform(features[:,1:3])

view = pd.DataFrame(features)

from sklearn.model_selection import train_test_split as tts

f_train,f_test, l_train, l_test = tts(features, labels,test_size=0.2,
                                      random_state=0)

