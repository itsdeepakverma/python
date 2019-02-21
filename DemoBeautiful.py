# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 13:47:13 2019

@author: Admin
"""

from bs4 import BeautifulSoup

import requests

with open("D:\\Python\\DataSet\\simple.html") as htmlfile:
    s=BeautifulSoup(htmlfile,'lxml')
    
    print(s)
    
    print(s.prettify())
    
    print(s.title)
    
    print(s.title.text)
    
    print(s.div)
    
    print(s.div.p.text)
    
    print(s.find('div'))
    
print(s.find('div',class_='footer'))
    
    
for article in s.find_all('div'):
    headline=s.p.text
    print(headline)

#reading a web page

source=requests.get("http://httpbin.org/html").text

s=BeautifulSoup(source,'lxml')
print (s.prettify())


print (s.head)

print (s.body)

print (s.body.h1)

print (s.body.div)

print (s.body.div.p)

print (s.body.div.p.text)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import requests
import unicodedata



#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source = requests.get(wiki).text
soup = BeautifulSoup(source)



print (soup.prettify())

all_tables=soup.find_all('table')

print (all_tables)


right_table=soup.find('table', class_='wikitable')

print (right_table)


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==5: #Only extract table body not heading
    
    
        A.append(str(cells[0].find(text=True)))
        B.append(str(states[1].find(text=True)))
        
        C.append(str(unicodedata.normalize('NFKD', cells[1].find(text=True)).encode('ascii','ignore')))
        
        D.append(str(unicodedata.normalize('NFKD', cells[2].find(text=True)).encode('ascii','ignore')))
        E.append(str(cells[3].find(text=True)))
        F.append(str(unicodedata.normalize('NFKD', cells[4].find(text=True)).encode('ascii','ignore')))


#import pandas to convert list to data frame
import pandas as pd

df=pd.DataFrame()
df['Admin_Capital']=A
df['State/UT']=B
df['Legislative_Capital']=C
df['Judiciary_Capital']=D
df['Year_Capital']=E
df["Former_Capital"] = F



df.to_csv("former.csv")
#print (df)