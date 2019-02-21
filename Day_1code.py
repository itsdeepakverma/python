# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:45:05 2018

@author: Admin
"""
import math
help(math.pi)

def Circle():
    a=int(input('Enter a number'))
    area=math.pi*math.pow(a,1)
    perimeter=2*math.pi*a
    
    print("Area of circle is {}".format(area))
    print("perimeter of circle is {}".format(perimeter))
def factorial():
    a=int(input('Enter a number'))
    b=math.pi*math.pow(a,1)
    print("Area of circle is {}".format(b))
def stringcase():
    a=input("Enter your name")
    #str=a.swapcase()
    #str1=a.title()
    str2=(a.lstrip('R')).replace('r','$')
    #print(str)
    #print(str1)
    print('R'+str2)
def stringswap():
    a=input('Enter your Name')
    str=a[a.find(" ")+1:]+" "+a[:a.find(" ")]
    print(str)
def quotation():
    print("\"Deepak\"""\n" "\"Verma\"" )
def degree():
    print( "26"u'\u00b0')
def unicode():
    print("unix"u'\u00AE'" AND SUN MICROSYSTEM "u'\u2122'" are "u'\u00A9'" ,2018 oracle")
def devnagri():
    print(u'\u0926'u'\u0940'u'\u092A'u'\u0915'", "u'\u0935'u'\u0930'u'\u094D'u'\u092E'u'\u093E')
def checker():
    for i in range(1,9):
        if(i%2==0):
            a=u'\u0952'" "u'\u0970'
            print(a*4)
        else:
            a=u'\u0970'" "u'\u0952'
            print(a*4)
def BMIHelpScreen():
    print("""World Health Organisation BMI Values(Level 8)
                Severe Thinness:less than 16
                Moderate Thinness:between 16 and 16.4
                Mild Thinness:between 17 and 18.4
                Normal:between 18.5 and 24.9
                Overweight:between 25 and 29.9
                Obese Class I:between 30 and 34.9
                Obese Class II:between 35 and 39.9
                Obese Class III: 40 and greater""")
    #a=input('enter')
    

def Main():
    print('Press 1 for circle')
    print('Press 2 for factorial')
    print('Press 3 for String case')
    print('Press 4 for string swap')
    choice=input("Enter Your Choice")
    if(choice=='1'):
        Circle()
    elif(choice=='2'):
        factorial()
    elif(choice=='3'):
        stringcase()
    elif(choice=='4'):
        stringswap()
    
Main()

