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
plt.show()

#graph for test set
plt.scatter(feature_test,label_test,color='red')

plt.plot(feature_train,regression.predict(feature_train),color='blue')

plt.title('Test Set')
plt.xlabel('Exprience in Year')
plt.ylabel("salary")


#woking on categarical data

data=pd.read_csv("D:\\python\\dataset\\Cricket_salary_Data.csv")
features=data.iloc[:,:-1].values
label=data.iloc[:,-1].values

from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values="NaN",strategy="mean",axis=0)
imputer=imputer.fit(features[:,1:2])
features[:,1:2]=imputer.transform(features[:,1:2])

#Encoding Categarical Data
#encoding Independent variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder=LabelEncoder()
features[:,0]=labelencoder.fit_transform(features[:,0])

#OnehotEncoder
onehotencoder=OneHotEncoder(categorical_features=[0])

features=onehotencoder.fit_transform(features).toarray()

label=labelencoder.fit_transform(label)

#Scaling of Data

df=pd.read_csv("D:\\python\\DataSet\\Cricket_Salary_Data.csv")

feature=df.iloc[:,:-1].values
label=df.iloc[:,-1].values

feature.isnull().any(axis=0)

#missing values handling

from sklearn.preprocessing import Imputer

imputer =Imputer(missing_values="NaN",strategy="mean",axis=0)

feature[:,1:2]=imputer.fit_transform(feature[:,1:2])

#labelencoding for categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder=LabelEncoder()
label=labelencoder.fit_transform(label)
feature[:,0]=labelencoder.fit_transform(feature[:,0])

onehotencoder=OneHotEncoder(categorical_features=[0])

feature=onehotencoder.fit_transform(feature).toarray()

from sklearn.model_selection import train_test_split as TTS

f_train,f_test,l_train,l_test=TTS(feature,label,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler

ss=StandardScaler()
f_train=ss.fit_transform(f_train)   
f_test=ss.transform(f_test)

#MultiLinear Regression


import pandas as pd
import numpy as np

df=pd.read_csv("D:\\python\\dataset\\Salary_Classification.csv")

feature=df.iloc[:,:-1].values
label=df.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split as TTS
from sklearn.linear_model import LinearRegression as LR
from sklearn.preprocessing import StandardScaler as SS

LE=LabelEncoder()

feature[:,0]=LE.fit_transform(feature[:,0])
OHE=OneHotEncoder(categorical_features=[0])

feature=OHE.fit_transform(feature).toarray()

#avoiding a dummy column

feature=feature[:,1:]

#spliting

f_train,f_test,l_train,l_test=TTS(feature,label,test_size=0.2,random_state=0)

# Scaling

ss=SS()
f_train=ss.fit_transform(f_train)


f_test=ss.transform(f_test)

# making Model

lr=LR()

lr.fit(f_train,l_train)

predictlabel=lr.predict(f_test)

scor=lr.score(f_train,l_train)

#backword elimination

import statsmodels.formula.api as SM

features=np.append(arr=np.ones((30,1)).astype(int), values=feature,axis=1)

feature_opt=features[:,[0,1,2,3,4,5]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=features[:,[0,1,3,4,5]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=features[:,[0,1,3,5]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=features[:,[0,3,5]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

feature_opt=features[:,[0,5]]
regressor_OLS=SM.OLS(endog=label, exog=feature_opt).fit()
regressor_OLS.summary()

#polynomial Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("D:\\python\\DataSet\\Position_Salaries.csv")
features=dataset.iloc[:,1:2].values
labels=dataset.iloc[:,2].values

#fitting Linearing regression to data
from sklearn.linear_model import LinearRegression

lr=LinearRegression()
lr.fit(features,labels)

#predicting values

print(lr.predict(6.5)[0])

plt.scatter(features,labels,color='red')
plt.plot(features,lr.predict(features),color='blue')
plt.title("Linear Regression")
plt.xlabel("position level")
plt.ylabel("Salaries")

#fitting ploynomial regression to data

from sklearn.preprocessing import PolynomialFeatures

poly=PolynomialFeatures(degree=4)

feature_poly=poly.fit_transform(features)

lr1=LinearRegression()
lr1.fit(feature_poly,labels)

#predicting values

print(lr1.predict(poly.fit_transform(6.5)))

plt.scatter(features,labels,color='red')
plt.plot(features,lr1.predict(poly.fit_transform(features)),color='blue')
plt.title("Polynomial Regression")
plt.xlabel("position level")
plt.ylabel("Salaries")

#polynomial regression for higher resolution and smoother curve

features_grid=np.arange(min(features),max(features),0.1)
features_grid=features.reshape(-1,1)
plt.scatter(features,labels,color='red')
plt.plot(features_grid,lr1.predict(poly.fit_transform(features_grid)),color='green')


#logistic Regression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

dataset=pd.read_csv("D:\\python\\dataset\\Social_Network_Ads.csv")

feature=dataset.iloc[:,[2,3]].values
label=dataset.iloc[:,4].values

ftrain,ftest,ltrain,ltest=tts(feature,label,test_size=0.2,random_state=0)

sc=StandardScaler()

ftrain=sc.fit_transform(ftrain)
ftest=sc.transform(ftest)

classifier=LogisticRegression(random_state=0)

classifier.fit(ftrain,ltrain)
predictlabel=classifier.predict(ftest)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(ltest,predictlabel)

#second sample code for logistic regression


from sklearn.datasets import load_iris

iris=load_iris()
print(iris.feature_names)

featrain,featest,labtrain,labtest=tts(iris.data,iris.target,test_size=0.25,random_state=0)

lc=LogisticRegression(random_state=0)
lc.fit(featrain,labtrain)

labpredic=lc.predict(featest)

cm1=confusion_matrix(labtest,labpredic)