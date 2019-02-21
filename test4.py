# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:03:35 2018

@author: Admin
"""

#file handling

#Read=r
#Write=w
#Append=a
#Create=x



try:
    file =open('D:\\Python\\game.txt','rt')
    print(file.name)
    print(file.mode)
except IOError:
    print("File not Found")
finally:
    file.close()
    

 #print(file.closed)

file.close()



with open('D:\\Python\\game.log','rt') as f:
    file_contents=f.read()
    print(file_contents)    

with open('D:\\Python\\game.log','rt') as f:
    file_contents=f.readline()
    print(file_contents) 
with open('D:\\Python\\game.log','rt') as f:
    file_contents=f.readlines()
    print(file_contents) 
    
    

with open('D:\\Python\\game.log','rt') as f:
    for line in f:
        print(line)

with open('D:\\Python\\game.log','rt') as f:
    file_contents=f.read(5)
    print(file_contents) 
    
    pos=f.tell()
    print(pos)
    f.seek(0)
    
    file_contents=f.read(5)
    print(file_contents)
    
    
with open('D:\\Python\\myfile.txt','at') as f:
    f.write("first line")
    f.writelines(["second line \n",'third line\n'])
    
with open('D:\\Python\\Demo.jpg','rb') as rf:
    with open('D:\\Python\\result.jpg','wb') as wf:
        for line in rf:
            wf.write(line)
            
import os

os.getcwd()

os.chdir('d:\\python')
os.getcwd()


os.path.exists('demo.jpg')

os.remove('demo.jpg')

os.makedirs('deepak')

os.rmdir('deepak')


import csv

with open('D:\\Python\\DataSet\\Salaries.csv') as cf:
        csvreader=csv.reader(cf,delimiter=',')
        for row in csvreader:
            print(row)
            
with open('D:\\Python\\DataSet\\Salaries.csv') as cf:
        csvreader=csv.reader(cf,delimiter=',')
        for row in csvreader:
            print(row[0])
            
with open('D:\\Python\\DataSet\\Salaries.csv') as cf:
        csvreader=csv.reader(cf,delimiter=',')
        next(csvreader)
        for row in csvreader:
            print(row)
            
with open('D:\\Python\\DataSet\\Salaries.csv') as cf:
        csvreader=csv.DictReader(cf,delimiter=',')
        for row in csvreader:
           # print(row)
           #print(row['salary'])
           print(row['rank'])
           
with open('D:\\Python\\DataSet\\demo.csv','w') as cf:
    demoWriter=csv.writer(cf,delimiter=',')
    
    demoWriter.writerow(['deepak','2000','jan'])

dir(csv)

