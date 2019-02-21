# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:27:48 2018

@author: Admin
"""


def main():
    str=input("enter numbers")
    list=str.split(',')
    flag=0
    sum=0
    for i in list:
        if(flag==1):
            flag=0
            continue
        if(i=='13'):
            flag=1
        else:
            sum+=int(i)
            
    print(sum)
    
main()