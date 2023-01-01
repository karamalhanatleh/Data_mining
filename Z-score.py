# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 13:58:44 2023

@author: Karam Alhanatlh
"""

#Z-score


import numpy as np 


"""
#z = ( x - μ ) / σ

z = Z-score
x = the value being evaluated
μ = the mean
σ = the standard deviation
"""

values = [4,5,6,6,6,7,8,12,13,13,14,18]

mean = sum(values) / len(values)
differences = [(value - mean)**2 for value in values]
sum_of_differences = sum(differences)
standard_deviation = (sum_of_differences / (len(values) - 1)) ** 0.5
#print(standard_deviation)



# Calculate the z-score from scratch
zscores = [(value - mean) / standard_deviation for value in values]

print(zscores)














