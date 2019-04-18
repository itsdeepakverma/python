# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:21:04 2019

@author: Admin
"""

import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv', header=None, usecols=[0,1,2])

df[0]=df['class label']

df=df.rename(columns={0:'class label',1:'Alcohol',2:'Malic Acid'})

from sklearn.preprocessing import StandardScaler as SS

ss=SS()


#standard scaling

df=ss.fit_transform(df)


# Min Max Scaling

from sklearn.preprocessing import MinMaxScaler as MMS

mms=MMS()

df_MMS=mms.fit_transform(df)

