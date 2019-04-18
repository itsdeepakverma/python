# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:10:18 2019

@author: Admin
"""

import pandas as pd

#df=pd.read_excel("D:\\OneDrive\\Documents\\JU\\Examination\\Jan 2019\\II In Sem\\Award list.xlsx")

ACAList=pd.read_excel("D:\\OneDrive\\Documents\\JU\\Examination\\Jan 2019\\II In Sem\\students\\ACA VIth sem.xlsx")

ACAList=ACAList.iloc[:,1:2]

Studentlist=pd.ExcelFile("D:\\OneDrive\\Documents\\JU\\Examination\\Jan 2019\\II In Sem\\Student_list.xlsx")

Section_A=Studentlist.parse(Studentlist.sheet_names[0])


Section_A["ACA"]=ACAList["Uni.Roll Number"].apply(lambda x:" " if x in str(Section_A["Roll NO"]) else "NOF")

#Studentlist.parse(Studentlist.sheet_names[0])["ACA"]=ACAList["Uni.Roll Number"].apply(lambda x:" " if x in str(Studentlist.parse(Studentlist.sheet_names[0])["Roll NO"]) else "NOF")

#for i in range(1):
 #   (Studentlist.parse(Studentlist.sheet_names[i]))["ACA"]=ACAList["Uni.Roll Number"].apply(lambda x:" " if x in str((Studentlist.parse(Studentlist.sheet_names[i]))["Roll NO"]) else "NOF")
    
    
writer=pd.ExcelWriter("D:\\Demo.xlsx","xlsxwriter")    
Section_A.to_excel(writer,"sheet1")



#Studentlist.parse(Studentlist.sheet_names[0]).to_excel(writer,"sheet1")