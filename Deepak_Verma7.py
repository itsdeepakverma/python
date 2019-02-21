# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:18:30 2018

@author: Admin
"""
def main():
    
    str=input("Enter string")
    listchar=list()
    listcnt=list()
    for i in str:
        if i in listchar:
            listcnt.insert(listchar.index(i),(listcnt.pop(listchar.index(i))+1))
        else:
            listchar.append(i)
            listcnt.append(1)
    
    a=0
    while(a<len(listchar)):
        print(listchar[a],':',listcnt[a])
        a=a+1

    

            
main()

