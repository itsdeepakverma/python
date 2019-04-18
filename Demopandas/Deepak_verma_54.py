# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:21:33 2019

@author: Admin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset=pd.read_csv("D:\\python\\dataset\\bluegills.csv")

features=dataset.iloc[:,0:1].values
labels=dataset.iloc[:,1].values

from sklearn.model_selection import train_test_split as tts

ftrain,ftest,ltrain,ltest=tts(features,labels,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression 
lr=LinearRegression()

lr.fit(ftrain,ltrain)

predictvalues=lr.predict(ftest)
print("length of 5 year old fish {}".format(lr.predict(5)))


#ploting

plt.scatter(ftest,ltest)
plt.plot(ftest,lr.predict(ftest),color="red")


#polynomial


from sklearn.preprocessing import PolynomialFeatures

poly=PolynomialFeatures(degree=4)
poly_features=poly.fit_transform(features)

pftrain,pftest,pltrain,pltest=tts(poly_features,labels,test_size=0.2,random_state=0)

lr1=LinearRegression()
lr1.fit(pftrain,pltrain)

polypredict=lr1.predict(pftest)

#plotting

plt.scatter(ftrain,ltrain)
plt.plot(ftrain,lr1.predict(poly.fit_transform(ftrain)),color='red')


print("length of 5 year old fish {}".format(lr1.predict(poly.fit_transform(5))))