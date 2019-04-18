# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:37:01 2019

@author: Admin
"""

import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("d:\\python\\dataset\\Mall_customers.csv")

feature=data.iloc[:,3:].values

#using elbow code to find the optimal no of cluster

from sklearn.cluster import KMeans

wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=0)
    kmeans.fit(feature)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)
plt.title("The Elbow Method")
plt.xlabel("NO. of cluster")
plt.ylabel("WCSS")
plt.show()

#fitting Kmeans to data set

kmeans=KMeans(n_clusters=5,init='k-means++',random_state=0)

Y_kmeans=kmeans.fit_predict(feature)

#visualization

plt.scatter(feature[Y_kmeans== 0,0],feature[Y_kmeans== 0,1],s=100,c='red',label='cluster1')

plt.scatter(feature[Y_kmeans== 1,0],feature[Y_kmeans== 1,1],s=100,c='blue',label='cluster2')

plt.scatter(feature[Y_kmeans== 2,0],feature[Y_kmeans== 2,1],s=100,c='green',label='cluster3')

plt.scatter(feature[Y_kmeans== 3,0],feature[Y_kmeans== 3,1],s=100,c='cyan',label='cluster4')

plt.scatter(feature[Y_kmeans== 4,0],feature[Y_kmeans== 4,1],s=100,c='magenta',label='cluster5')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='yellow',label='centroids')

plt.title('cluster of customers')

plt.xlabel('annual income')

plt.ylabel('spending score(1-100)')

plt.legend()

plt.show()