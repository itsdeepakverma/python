# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:05:50 2019

@author: Admin
"""

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests

websource="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"

source=requests.get(websource).text

s=BeautifulSoup(source,'lxml')

table=s.find('table',class_='wikitable')

A=[]
B=[]

for row in table.findAll('tr'):
    cells=row.findAll('th')
    states=row.findAll('td')
    if len(states)==7:
        A.append(states[1].find(text=True))
        B.append(states[4].find(text=True))


#plt.rcdefaults()
VALUES=B[:6]
LABELS=A[:6]
explode=[.2,0,0,0,0,0]
plt.pie(VALUES,labels=LABELS,explode=explode,autopct='%.2f')
plt.show()