# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:29:40 2019

@author: Admin
"""

import pandas as pd

from sklearn.model_selection import train_test_split as TTS
from sklearn.linear_model import LinearRegression as LR
import matplotlib.pyplot as plt


df=pd.read_csv("D:\\Python\\DataSet\\Bahubali2_vs_Dangal.csv")

feature=df.iloc[:,0:1].values
B_label=df.iloc[:,1].values
D_label=df.iloc[:,2].values

#model for Bahubali2

bf_train,bf_test,bl_train,bl_test=TTS(feature,B_label,test_size=0.2,random_state=0)

lr=LR()

lr.fit(bf_train,bl_train)

predictB=lr.predict(bf_test)

B10days=lr.predict(10)


#model for Dangal

df_train,df_test,dl_train,dl_test=TTS(feature,D_label,test_size=0.2,random_state=0)

lr1=LR()
lr1.fit(df_train,df_train)

predictD=lr1.predict(df_test)

D10days=lr1.predict(10)

if(B10days>D10days):
    print("Bahubali will collect more and collection is {}".format(B10days))
else:
    print("Dangal will collect more and collection is {}".format(D10days))

