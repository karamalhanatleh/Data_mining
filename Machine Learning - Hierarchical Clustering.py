# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 12:49:26 2022

@author: Karam Alhanatlh

"""
#Machine Learning - Hierarchical Clustering


## import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering



# x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]


# ## vizulat 
# plt.scatter(x, y)
# plt.show()




# data = list(zip(x, y))

# linkage_data = linkage(data, method='ward', metric='euclidean')
# dendrogram(linkage_data)

# plt.show()







from sklearn.cluster import AgglomerativeClustering

# x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
# y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]


# # data = list(zip(x, y))

# # hierarchical_cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
# # labels = hierarchical_cluster.fit_predict(data)

# # plt.scatter(x, y, c=labels)
# # plt.show()
# # #




# x = [ 3, 5, 10,8, 12, 1, 0 ,7 ,2,7] # hours
# y = [ 66,75,89,81,99,19,0 ,79,32,55]  #gradge

# data = list(zip(x,y))

# h_c= AgglomerativeClustering(n_clusters=2 , affinity='euclidean' , linkage='ward')
# la=h_c.fit_predict(data)

# plt.scatter(x, y, c= la) 
# plt.show()




# x=[40,32,50, 24, 60,72,12,19,35] # age
# y=[37 ,29,76 ,19 ,121,89,2 ,5, 42] # mony a thousand

# data = list(zip(x,y))
# h_cl = AgglomerativeClustering(n_clusters=2 , affinity='euclidean' , linkage='ward')#Manhattan
# labels_cluster = h_cl.fit_predict(data) 

# plt.scatter(x,y,c= labels_cluster)
# plt.show()

















