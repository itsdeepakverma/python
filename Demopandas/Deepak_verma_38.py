# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 15:31:14 2019

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt



data=np.random.normal(150,20,1000)

plt.hist(data,100)
print("Standard deviation is :{}".format(np.std(data)))

print("Variance is :{}".format(np.var(data)))



