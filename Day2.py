# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:03:44 2018

@author: Admin
"""

if (5>6):
    print("yes")
#eilf():
 #eilf(): 
else:
    print("NO")
    
# and or ! used for logical operator
    
    x=None
    bool(x)
n=0
while (n<10):
    print(n)
    n=n+1
    
    #List
    
empty_list=[1,2,3,4,5,2.3,"hi"]
#empty_list= list()
print(type(empty_list))
empty_list=[1,2,3,4,5]

empty_list.sort()
#sorted(empty_list) global function

empty_list.append(6)
empty_list.insert(0,89)
empty_list.remove(89)

empty_list.pop()

#del empty_list[0:]
print(empty_list)


x=[0,1,2]

y=[4,5,6]

    
x.append(y)

x.extend(y)
print(x)

x=list(range(10))
print(x)

for i in x:
    if(i%2==1):
        pass 
        #print("{}%2".format(i))
    print(i)
    
class MyClass(object):
    def meth_a(self):
        pass

    def meth_b(self):
        print ("I'm meth_b")





def heell(ar):
    return "hello {}".format(ar)

print(heell("Deepak"))

a,b,r=1,2,"dejd"
print(a)
print(b)
print(r)
#tuples
c=(2,3)#packing
print(type(c))

d,e=c#unpacking
print(d)
print(e)

Days=('Monday','Tuesday','wednesday','Thursday','Friday','Saturday')
print(Days)

a=1
b=2
#swapping
a,b=b,a

x,y=divmod(23,2)
help(enumerate)
for index,item in enumerate(Days):
    print("{} : {}".format(index,item))
    
    
for step in enumerate(Days):
    print("{} : {}".format(step[0],step[1]))
    
for step in enumerate(Days):
    print("{} : {}".format(*step))

help(str.join)