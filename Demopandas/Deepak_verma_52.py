# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 16:43:08 2019

@author: Admin
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as SST
from sklearn.linear_model import LinearRegression as LR

df=pd.read_csv("D:\\python\\dataset\\iq_size.csv")

feature=df.iloc[:,1:].values
label=df.iloc[:,0].values

f_train,f_test,l_train,l_test=SST(feature,label,test_size=0.2,random_state=0)

lr=LR()
lr.fit(f_train,l_train)

predictlabel=lr.predict(f_test)

x=[90,70,150]
a=np.array(x)
a=a.reshape(1,-1)


print("IQ lavel for given attribute is {}".format(lr.predict(a)))

#optimize model for the problem

import statsmodels.formula.api as SM

features=np.append(arr=np.ones((38,1)).astype(int), values=feature,axis=1)

feature_opt=features[:,[0,1,2,3]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=features[:,[0,1,2]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=features[:,[1,2]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=features[:,[1]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()



