# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:06:26 2019

@author: Admin
"""

import pandas as pd

df=pd.read_csv("D:\\Python\\DataSet\\Foodtruck.csv")

# checking missing values

df.isnull().any(axis=0)

#no missing valuse in the dataset

feature=df.iloc[:,:-1].values
label=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split as TTS
from sklearn.linear_model import LinearRegression as LR
import matplotlib.pyplot as plt


f_train,f_test,l_train,l_test=TTS(feature,label,test_size=0.2,random_state=0)

lr=LR()
lr.fit(f_train,l_train)

labelpredict=lr.predict(f_test)

#model score

score=lr.score(f_test,l_test)

#training set graph

plt.scatter(f_train,l_train,color='red')
plt.plot(f_train,lr.predict(f_train), color='blue')

plt.title('training set')
plt.xlabel('profit')
plt.ylabel('population')


# for test set

plt.scatter(f_test,l_test,color='red')
plt.plot(f_test,lr.predict(f_test), color='blue')

plt.title('test set')
plt.xlabel('profit')
plt.ylabel('population')


#prediction for Jaipue outlet

result=lr.predict(3.073)

print("prediction for jaipur outlet is {}".format(result))

