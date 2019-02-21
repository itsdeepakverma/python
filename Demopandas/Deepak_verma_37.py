# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:46:50 2019

@author: Admin
"""

import numpy as np

import matplotlib.pyplot as plt

income=np.random.normal(100,20,10000)

plt.hist(income, 50)
#mean
print("mean of generated data is {}".format(np.mean(income)))
#median
print("Medien of Generated data is{}".format(np.median(income)))
#adding outliers to the data set


income=np.append(income,[10000000])
#mean after outliers

print("mean of generated data is {}".format(np.mean(income)))
#median
print("Medien of Generated data is{}".format(np.median(income)))