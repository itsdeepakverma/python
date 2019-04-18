1# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:05:38 2018

@author: Admin
"""

#for and while with else

# 

import logging

#debug
#info


#warning
##error
#Critical

#logging.basicConfig(level=logging.DEBUG)

logging.basicConfig(filename='game.log',level=logging.DEBUG)


logging.debug("Debugging msg")
logging.info("info msg")
logging.warn("warn msg")
logging.error("error msg")
logging.critical("critical msg")

dict1=dict()

print(type(dict1))

dict1={}

dict1=dict({})

dict1={"fname":"deepak","lname":"verma",'age':'32'}
print(dict1)

dict1['fname']='Rajesh'
print(dict1)


#adding new key

dict1['address']='jaipur'


dict1.update({'age':34,'address':'kota'})



#printing

print(dict1['fname'])

print(dict1.get('fname'))
print(dict1.get('fname','Not found'))

str1="hi my name is {name} and i live in {address}".format(name='jone',address='ajmer')

print(str1)
print(str1)
del dict1['address']

dict1.pop('address')

#to list all kyes

dict1.keys()

dict1.values()

for key in dict1.keys():
    print(key)
    
for values in dict1.values():
    print(values)

for key in dict1.keys():
    print(key,dict1[key])

for key,value in dict1.items():
    print(key,value)



w=['one','two','one','three','four']
f=dict()
for i in w:
    if i in f:
        f[i]+=1
    else:
        f[i]=1

for i in f.keys():
    print(i,":",f[i])
    
    
from collections import Counter

w=['one','two','one','three','four']

f=Counter(w)
print(f)


#orderedDict
#namedtuple
#deque