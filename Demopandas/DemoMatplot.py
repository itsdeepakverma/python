# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:05:17 2019

@author: Admin
"""

# draw line graph
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-3,3,0.001)

plt.plot(x,norm.pdf(x))

#multiple plot on one grapf

plt.plot(x,norm.pdf(x))
plt.plot(x,norm.pdf(x,1.0,0.5))

#save a graph

plt.savefig("result",format="png")


#adjust the axis

axis=plt.axes()
axis.set_xlim([-5,5])
axis.set_ylim([0,1.0])

axis.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axis.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
plt.plot(x,norm.pdf(x))


#add a grid

axis=plt.axes()
axis.set_xlim([-5,5])
axis.set_ylim([0,1.0])

axis.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axis.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
axis.grid()
plt.plot(x,norm.pdf(x))



#change line color

axis=plt.axes()
axis.set_xlim([-5,5])
axis.set_ylim([0,1.0])

axis.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axis.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
axis.grid()
plt.plot(x,norm.pdf(x),'r')
plt.show()

# adding labels

axis=plt.axes()
axis.set_xlim([-5,5])
axis.set_ylim([0,1.0])

axis.set_xticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
axis.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
axis.grid()
plt.xlabel("x values")
plt.ylabel("y values")

plt.plot(x,norm.pdf(x,1.0,0.5))
plt.plot(x,norm.pdf(x),'r')
plt.legend(['sneetches','gacks'],loc=1)
plt.show()


#pie chart

plt.rcdefaults()
values=[12,55,1,32,14]
color=['r','g','b','c','m']
explode=[0,0,0,0.2,0]
labels=['A','B','C','D','E']
plt.pie(values,colors=color,explode=explode,labels=labels,autopct='%.2f')
plt.title('students location')
plt.show()


#bar chart

plt.rcdefaults()
values=[12,55,1,32,14]
color=['r','g','b','c','m']
plt.bar(range(0,5),values,color=color)
plt.show()

#scatter

from pylab import randn
x=randn(500)
y=randn(500)

plt.scatter(x,y)

#histogram

incomes=np.random.normal(27000,15000,10000)
plt.hist(incomes,50)

#box and whisker plot

unifromskewed=np.random.rand(100)*100-40

high_outliers=np.random.rand(10)*50+100
low_outliers=np.random.rand(10)*-50-100

data=np.concatenate((unifromskewed,high_outliers,low_outliers))
plt.boxplot(data)

