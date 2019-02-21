# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 13:02:47 2018

@author: Admin
"""

def Main():
    str=input("Enter the input")
    a=str[str.find(" "):] + " " + str[:str.find(" ")]
    print(a)

Main()


