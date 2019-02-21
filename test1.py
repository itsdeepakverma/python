# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:50:34 2018

@author: Admin
"""

def main():
    #name = input("enter your name")
    #print(type(name))
    #print(name)
    a="""hi this is deepak verma
            form Ju
        """
    print(a)
main()

"hello"+str(5)
"Deepak"*5
print("Deepak's")
print("\"Deepak\"")
print("\\Deepak\\")
print(u'\u0065')
import math
dir(math)
help(math.sqrt)
math.sqrt(25)

import math as mt
mt.pow(2,4)

from math import sqrt as sq
sq(25)
import random
random.randint(0,10)

import os
os.system("cls")

str="Deepak Verma"
c=str.split()
print(c)
#str[-1]
#str[3:10]
#str[:10]
#str[0:]
#str[-1:]
#str[-6:]
str[::2]
str[::-2]
len(str)
#del(str) use for deleting from stack
str.lower()
str.find('a')
str.replace('a','\n')
str.lstrip('D')
str.rstrip('a')
str.strip('e')
str.find('a',2,12)
help(str.lstrip)

type(c)

age=33
print("Hello {} you are {} years old".format(str,age))

#openedx.forsk.in