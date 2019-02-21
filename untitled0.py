# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:18:30 2018

@author: Admin
"""
#letter frequency calculater
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
    print(listchar)
    print(listcnt)
            
main()


#Age Calculter
from datetime import date
def AgeCal(dob):
    currentdate=date.today()
    age=currentdate.year-dob.year -((currentdate.month,currentdate.day)<(dob.month,dob.day))
    print(age)

AgeCal(date(1984,5,18))


# Height calculator

def HeightCal():
    a=float(input('enter your height'))
    print('Height in Meters is {}'.format(a*0.3048))
    print('Height in Cetimeter is {}'.format(a*0.3048*100))
    
#Body mass index calculater and Ponderal Index
def BMI():
    height= float(input('Enter your height in meters'))
    weight= float(input('Enter your weight in KG'))
    Bmi=(weight/height)/height
    print('your BMI is {}'.format(Bmi))    
    print('your Ponderal index is {}'.format(Bmi/height))

# Heart rate calculator
def heartrate():
    Age=int(input('Enter your Age'))
    MHR=220-Age
    MTHR=MHR*0.7
    MaTHR=MHR*0.85
    print('your maximum heart rate is {}'.format(MHR))
    print('Your range for targate heart rate is ({},{})'.format(MTHR,MaTHR))

#temperture Calculater
def Temperture():
    today_temp=int(input('enter today temperture in degree centigrade'))
    tempInFahren=today_temp*(9/5) + 32
    TempInKalvin=today_temp+273
    print('temperture in fahrenheit is {} and in Kalvin is {}'.format(tempInFahren,TempInKalvin))
    
#	Remove all the vowels from the list of states
def Vowel():
    statelist=['Rajasthan','Bihar','uttar pradesh']
    result=list()
    vowel=['a','e','i','o','u']
    for state in statelist:
        newstr=state
        for x in state:
            if x in vowel:
                newstr=newstr.replace(x,'')
        #print(newstr)
       # print(statelist)
        result.insert(statelist.index(state),newstr)
    print(result)
                
#Shopping List
ItemList=list()
def addItem(item):
    if item not in ItemList:
        ItemList.append(item)
    else:
        print('{} is already in the list'.format(item))
def addItems():
    Items=input('Enter items for adding in the list')
    ItemList.extend(Items.split(','))
def Display():
    print("""What do you want
              Enter Shop for start shopping
              Enter Shop MUltiple for more than one Item
              Enter Insert for insertion
              Enter Help for display Menu
              Enter Show to See list in your cart
              Enter Done for Exit
              """)
    c=input('Enter Your Choice')
    return c

def randomInsert():
    location=int(input("Enter location for insertion"))
    value=input("Enter value for insertion")
    if len(ItemList) < location:
        print("Invalid location")
    else:
        ItemList.insert(location,value)
def remove():
    location=int(input('Enter index poition to delete item'))
    value=ItemList.pop(location)
    print('deleted item is={}'.format(value))

def show():
    for x in ItemList:
        print(x)

def ShoppingApp():
    cammond=Display()
    while cammond.upper()!='DONE':
        if cammond.upper()=='SHOP':
            item=input('Enter Item to add in the list')
            addItem(item)
            cammond=Display()
        elif cammond.upper()=='SHOP MULTIPLE':
            addItems()
            cammond=Display()
        elif cammond.upper()=='SHOW':
            show()
            cammond=Display()
        elif cammond.upper()=='HELP':
            cammond=Display()
        elif cammond.upper()=='DONE':
            break
        elif cammond.upper()=='INSERT':
            randomInsert()
            cammond=Display()
        elif cammond.upper()=='REMOVE':
            remove()
            cammond=Display()
        
        
        #cammond=input('Enter your Choice')
        
    #print(ItemList)
   
ShoppingApp()



 #hangman
import random
def hangman():
    WList=["Mango","Orange","Grapes",]
    index=random.randint(0,len(WList))
    sword=list(WList[index].lower())
    #print(sword)
    
    cnt=0
    flag=0
    result=list(" "*len(sword))
    print(result)
    
    while cnt<len(sword):
        letter=input('enter your guess')
        if letter in sword:
            result.pop(sword.index(letter))
            result.insert(sword.index(letter),letter)
        else:
            print("Not in the Word")
            flag+=1
            
        print(result)
       # letter=input('enter your guess')    
        cnt=cnt+1
    if flag==0:
        print("you won:")
    else:
        print("Computer Won:")

hangman() 

#Zoo.CSV

import csv

with open("D:\Python\\zoo.csv") as cf:
    csvreader=csv.reader(cf,delimiter=',')
    for row in csvreader:
        print(row)

with open("D:\Python\\zoo.csv") as cf:
    cv=csv.reader(cf,delimiter=',')
    e_sum=t_sum=z_sum=l_sum=k_sum=0
    for row in cv:
        if row[0]=='elephant':
            e_sum+=int(row[2])
        if row[0]=='tiger':
            t_sum+=int(row[2])
        if row[0]=='zebra':
            z_sum+=int(row[2])
        if row[0]=='lion':
            l_sum+=int(row[2])
        if row[0]=='kangaroo':
            k_sum+=int(row[2])
    print("elephant needed {} watre".format(e_sum))
    print("tiger needed {} watre".format(t_sum))
    print("zebra needed {} watre".format(z_sum))
    print("lion needed {} watre".format(l_sum))
    print("kangaroo needed {} watre".format(k_sum))
        

with open("D:\Python\\zoo.csv") as cf:
     cv=csv.reader(cf,delimiter=',')
     e_sum=0
     next(cv)
     for row in cv:
        #print(row[2])
        e_sum+=int(row[2])  
     print("All needed {} water".format(e_sum))


#We will write a Python program to read through the lines of the file, break each line into a list of words, and then loop through each of the words in the line, and count each word using a dictionary.     
     
fc=dict()
with open("D:\\Python\\romeo.txt","rt") as file:
    filecontent=file.readlines()
    #print(filecontent)
    for x in filecontent:
        xl=x.split(" ")
        for y in xl:
            if y in fc:
                fc[y]+=1
            else:
                fc[y]=1

for k,v in fc.items():
    print(k,v)

#Find hash of a file using hashlib library and using SHA-1 algorithm
import hashlib

str="this is deepak verma"
result=hashlib.sha1(str.encode())
print(result.hexdigest())



#Find the resolution of any jpeg Image file ( width x height )

from PIL import Image
im=Image.open("D:\\Python\\result.jpg")
a=im.size
print(a)

#With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
#write a program to make a list whose elements are intersection of the above given lists.

a=set([1,3,6,78,35,55])
b=set([12,24,35,24,88,120,155])
c=a&b
print(c)

#With a given list [12,24,35,24,88,120,155,88,120,155], write a 
#program to print this list after removing all duplicate values with original order reserved.
a=set([12,24,35,24,88,120,155,88,120,155])
print(a)
b=list(a)[::-1]
print(b)

from PIL import Image
import os

strdir=os.getcwd()
imname=input("enter image name")
if os.path.exists(imname+".jpg"):
    dirname=strdir+"\\"+imname+".jpg"
    im=Image.open(dirname)
    out=im.convert('L')
    outr=im.transpose(Image.ROTATE_90)
    #outr.show()
    box=(160,161,203,204)
    outc=im.crop(box)
    outc.save(strdir+"\\outc.jpg")
    #outc.show()
    size=(75,75)
    outt=strdir+"\\"+imname+".thumbnail"
    im.thumbnail(size)
    im.save(outt,"JPEG")
    im.show()


from PIL import Image
import os

strdir=os.getcwd()
item=os.listdir(".")
imagelist=list()
for n in item:
    if n.endswith(".jpg"):
        imagelist.append(n)
print(imagelist)

import sys

a="srt der"
sys.getsizeof(a)
