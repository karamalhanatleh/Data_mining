# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:42:47 2022

@author: Karam Alhanatlh
"""

# import  packages

import numpy as np
from numpy.linalg import norm




A = np.array([2,1,2,3,2,9])
B = np.array([3,4,2,4,5,5])



# compute cosine similarity
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity:", cosine)



A = np.array([5, 0, 3, 0, 2, 0, 0, 2, 0, 0])
B = np.array([3, 0, 2, 0, 1, 1, 0, 1, 0, 1])



# compute cosine similarity
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity:", cosine)
