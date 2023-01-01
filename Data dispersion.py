# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 11:49:32 2023

@author: Karam Alhanatlh
"""

#packages
import numpy as np



def detect_outlier(data):
    # find q1 and q3 values
    q1, q3 = np.percentile(sorted(data), [25, 75])
 
    # compute IRQ
    iqr = q3 - q1
 
    # find lower and upper bounds
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
 
    outliers = [x for x in data if x <= lower_bound or x >= upper_bound]
 
    return outliers

def d_dis(x):
    x=list(x)
    print("median : " ,np.median(x))
    print("max    : " ,np.max(x))
    print("min    : " ,np.min(x))
    print("outliers  : ", detect_outlier(x))
    print("variance  : ", np.var(x))

    a=np.array(x)
    print("quantile 0.25 : " ,  np.quantile(a, 0.25))
    print("quantile 0.50 : " ,  np.quantile(a, 0.50))
    print("quantile 0.75 : " ,  np.quantile(a, 0.75))




n1=[1,2,3,3,3,8,70]    
d_dis(n1)


 
