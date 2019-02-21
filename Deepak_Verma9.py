# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:59:44 2018

@author: Admin
"""

dir(list)
help(list.pop)
list=[1,2,3,4,5,6,7]
print(sum(list)//len(list))

def main():
    str=input("enter values")
    list=str.split(',')
    type(int(list[0]))
    l1=[]
    i=0
    while(i<len(list)):
        l1.append(int(list[i]))
        i+=1
    
    l1.pop(l1.index(min(l1)))
    l1.pop(l1.index(max(l1)))
    
    print('mean of array is={}'.format(sum(l1)//len(l1)))
    
main()