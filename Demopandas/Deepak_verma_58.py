# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:01:19 2019

@author: Admin
"""

"""
This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon Society Field Guide to North American Mushrooms (1981). Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended. This latter class was combined with the poisonous one.

 

Attribute Information:

classes: edible=e, poisonous=p (outcome)

cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s

cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s

cap-color: brown=n, buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y

 

bruises: bruises=t, no=f

 

odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,pungent=p,spicy=s

 

gill-attachment: attached=a,descending=d,free=f,notched=n

 

gill-spacing: close=c,crowded=w,distant=d

 

gill-size: broad=b,narrow=n

 

gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g,

green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y

 

stalk-shape: enlarging=e,tapering=t

 

stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?

 

stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s

 

stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s

 

stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y

 

stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,red=e,white=w,yellow=y

 

veil-type: partial=p,universal=u

 

veil-color: brown=n,orange=o,white=w,yellow=y

ring-number: none=n,one=o,two=t

 

ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p,sheathing=s,zone=z

 

spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o,purple=u,white=w,yellow=y

 

population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y

 

habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d

Perform Classification on the given dataset to predict if the mushroom is edible or poisonous w.r.t. it’s different attributes.
(you can perform on habitat, population and odor as the predictors)

Check accuracy of the model.

"""

import pandas as pd


data=pd.read_csv("D:\\python\\dataset\\mushrooms.csv")

feature=data.iloc[:,list(data.columns).index('odor'):list(data.columns).index('odor')+1]

feature[data.columns[list(data.columns).index('habitat')]]=data.iloc[:,list(data.columns).index('habitat'):list(data.columns).index('habitat')+1]

feature[data.columns[list(data.columns).index('population')]]=data.iloc[:,list(data.columns).index('population'):list(data.columns).index('population')+1]

feature=feature.values

label=data.iloc[:,list(data.columns).index('class')].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

odor=LabelEncoder()
habitat=LabelEncoder()
population=LabelEncoder()


feature[:,0]=odor.fit_transform(feature[:,0])

feature[:,1]=habitat.fit_transform(feature[:,1])

feature[:,2]=population.fit_transform(feature[:,2])


odorOHE=OneHotEncoder(categorical_features=[0])

feature=odorOHE.fit_transform(feature).toarray()

habitatOHE=OneHotEncoder(categorical_features=[9])

feature=habitatOHE.fit_transform(feature).toarray()

populationOHE=OneHotEncoder(categorical_features=[16])

feature=populationOHE.fit_transform(feature).toarray()

from sklearn.model_selection import train_test_split as TTS


ftrain,ftest,ltrain,ltest=TTS(feature,label,test_size=0.2,random_state=0)


from sklearn.neighbors import KNeighborsClassifier

classifier=KNeighborsClassifier(n_neighbors=5,p=2)

classifier.fit(ftrain,ltrain)


pred=classifier.predict(ftest)

from sklearn.metrics import confusion_matrix

cm=confusion_matrix(ltest,pred)





