# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:34:03 2019

@author: Admin
"""
import numpy as np


nparray=np.random.randint(5,15,60)
#nparray=np.linspace(5,15,40)

nparray=np.array(nparray,dtype='int64')

val,cnt=np.unique(nparray,return_inverse=True)

val[np.argmax(np.bincount(cnt))]


#with out np
from collections import Counter

a=Counter(nparray)
print(a)