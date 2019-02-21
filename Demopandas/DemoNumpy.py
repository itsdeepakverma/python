# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:18:30 2019

@author: Admin
"""

import numpy as np

income=np.random.normal(27000,15000,10000)
np.mean(income)

import matplotlib.pyplot as plt

plt.hist(income,50) 
plt.show()


np.median(income)

#adding outliers

income=np.append(income,[1000000000])

np.median(income)

np.mean(income)

income1=np.random.normal(100.0,50.0,10000)

plt.hist(income1)

plt.show()

print(income1.std())

print(income1.var())



