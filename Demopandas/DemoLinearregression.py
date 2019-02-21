# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 17:27:56 2019

@author: Admin
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv("D:\\Python\\DataSet\\Income_Data.csv")

feature=dataset.iloc[:,0:1].values
labels=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split

feature_train,feature_test,label_train,label_test=\
train_test_split(feature,labels,test_size=0.2,random_state=0)


from sklearn.linear_model import LinearRegression

regression=LinearRegression()

regression.fit(feature_train,label_train)

labelpredict=regression.predict(feature_test)

# model score

score=regression.score(feature_test,label_test)


#graph for train set
plt.scatter(feature_train,label_train,color='red')

plt.plot(feature_train,regression.predict(feature_train),color='blue')


plt.title("Training set")
plt.xlabel("Exprience in year")
plt.ylabel("Salary in Rs.")
plt.savefig("Result")


#graph for test set
plt.scatter(feature_test,label_test,color='red')

plt.plot(feature_train,regression.predict(feature_train),color='blue')

plt.title('Test Set')
plt.xlabel('Exprience in Year')
plt.ylabel("salary")
