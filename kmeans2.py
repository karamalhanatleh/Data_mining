# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 15:48:10 2022

@author: Karam Alhanatlh
"""
"""
import matplotlib.pyplot as plt
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

plt.scatter(x, y)
plt.show()


from sklearn.cluster import KMeans


data = list(zip(x, y))
inertias = []



for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x,y, c=kmeans.labels_)
plt.show()


#########

t1=[1,2,8,11]
t2=[2,2,12,15]
d = list(zip(t1,t2))
plt.scatter(t1,t2)
plt.show()

km =KMeans(n_clusters=2)
km.fit(d)
plt.scatter(t1,t2,c=km.labels_)
plt.show()

"""


import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
plt.scatter(x, y)
plt.show()



data = list(zip(x, y))
print(data)



inertias = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()


kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()

