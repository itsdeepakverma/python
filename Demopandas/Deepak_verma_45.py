# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:46:46 2019

@author: Admin
"""

import pandas as pd
dataframe=pd.read_csv("D:\\python\\DataSet\\Automobile.csv")

print("Data type is {}".format(type(dataframe)))

ObjectDataFrame=dataframe.select_dtypes(include="object", exclude=None)

dataframe.isnull().any(axis=0)


#for filling nan with most occuring values

dataframe=dataframe.apply(lambda x: x.fillna(x.value_counts().index[0]))

#label encoding

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split

feature=dataframe.iloc[:,:-1].values
label=dataframe.iloc[:,-1].values



#onehotencoder=OneHotEncoder(categorical_features=[taframe.columns.get_loc('body_style'),dataframe.columns.get_loc('drive_wheels')])

#dataframe.iloc[:,dataframe.columns.get_loc('body_style')]=labelencoder.fit_transform(dataframe.iloc[:,dataframe.columns.get_loc('body_style')])

#dataframe.iloc[:,dataframe.columns.get_loc('drive_wheels')]=labelencoder.fit_transform(dataframe.iloc[:,dataframe.columns.get_loc('drive_wheels')])

list=[2,3,4,5,6,7,8,14,15,17]#column no of categorical data
for x in list:
    labelencoder=LabelEncoder()
    feature[:,x]=labelencoder.fit_transform(feature[:,x])

for x in list:
    onehotencoder=OneHotEncoder(categorical_features=[x])
    feature=onehotencoder.fit_transform(feature).toarray()


