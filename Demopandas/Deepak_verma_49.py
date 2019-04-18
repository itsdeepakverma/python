# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 12:02:12 2019

@author: Admin
"""

import pandas as pd

df=pd.read_csv("D:\\Python\\DataSet\\Red_Wine.csv")

df.isnull().any(axis=0)


#handing numeric values
from sklearn.preprocessing import Imputer

imputer=Imputer(missing_values="NaN",strategy="mean",axis=0)

df.iloc[:,1:12]=imputer.fit_transform(df.iloc[:,1:12])

#df_new.isnull().any(axis=0)


#handling categorical missing values


df_new=df.apply(lambda x: x.fillna(x.value_counts().index[0]))


from sklearn.model_selection import train_test_split as TTS
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.preprocessing import StandardScaler

feature=df_new.iloc[:,:-1].values
label=df_new.iloc[:,-1].values

LE=LabelEncoder()

feature[:,0]=LE.fit_transform(feature[:,0])

OHE=OneHotEncoder(categorical_features=[0])

feature=OHE.fit_transform(feature).toarray()
ss=StandardScaler()
feature=ss.fit_transform(feature)

f_train,f_test,l_train,l_test=TTS(feature,label,test_size=0.2,random_state=0)

