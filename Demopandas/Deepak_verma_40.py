# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:46:25 2019

@author: Admin
"""
import numpy as np
a=input("enter values")
list=(a.split(" "))

nparr=np.array(list)

nparr=nparr.astype(int)
np.reshape(nparr,(3,3))