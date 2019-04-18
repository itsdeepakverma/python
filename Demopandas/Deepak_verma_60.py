# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 22:02:13 2019

@author: Admin
"""

"""
Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

Perform K-means clustering to distinguish urban drivers and rural drivers.
Perform K-means clustering again to further distinguish speeding drivers from those who follow speed limits, in addition to the rural vs. urban division.
Label accordingly for the 4 groups.


"""

import pandas as pd

data=pd.read_csv("D:\\python\\dataset\\deliveryfleet.csv")

import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("d:\\python\\dataset\\deliveryfleet.csv")

feature=data.iloc[:,1:].values

from sklearn.cluster import KMeans

kmeans=KMeans(n_clusters=2,init='k-means++',random_state=0)

Y_kmeans=kmeans.fit_predict(feature)

#visualization

plt.scatter(feature[Y_kmeans== 0,0],feature[Y_kmeans== 0,1],s=100,c='red',label='Rural')

plt.scatter(feature[Y_kmeans== 1,0],feature[Y_kmeans== 1,1],s=100,c='blue',label='Urban')



plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='yellow',label='centroids')



plt.xlabel('Distance')

plt.ylabel('Speed')

plt.legend()

plt.show()

#for 4 clusters

kmeans=KMeans(n_clusters=4,init='k-means++',random_state=0)

Y_kmeans=kmeans.fit_predict(feature)

#visualization

plt.scatter(feature[Y_kmeans== 0,0],feature[Y_kmeans== 0,1],s=100,c='red',label='Urban Not Follow')

plt.scatter(feature[Y_kmeans== 1,0],feature[Y_kmeans== 1,1],s=100,c='blue',label='Rural Not Follow')

plt.scatter(feature[Y_kmeans== 2,0],feature[Y_kmeans== 2,1],s=100,c='green',label='urban follow')

plt.scatter(feature[Y_kmeans== 3,0],feature[Y_kmeans== 3,1],s=100,c='pink',label='Rural follow')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='yellow',label='centroids')



plt.xlabel('Distance')

plt.ylabel('Speed')

plt.legend()

plt.show()
