# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:35:26 2018

@author: Admin
"""

help(str.isdigit)

def main():
    str=input("enter your string")
    digit=0
    char=0
    i=0
    while(i<len(str)):
        if(str[i].isalpha()):
            char+=1
        if(str[i].isnumeric()):
            digit+=1
            
        i+=1
    
    print("char= {}".format(char))
    print("digit= {}".format(digit))
    
main()