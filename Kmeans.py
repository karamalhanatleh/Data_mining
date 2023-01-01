# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 19:07:46 2022

@author: Karam Alhanatlh
"""

"""
  Kmeans 
 used to Manhattan distance  
 |x1 — x2| + |y1 — y2|
"""

# import packages


def Manhattan_distance(x2,x1 , y2,y1):
    md=  abs((x2-x1) + abs(y2-y1) )
    return " Manhattan distance : " ,md

#def Manhattan_distance2(**k):



def myFun(k , n):
    
    k=list(k)
    n=list(n)
    for a,s in zip(k,n):
        print(a, k ,)
myFun([1,2,3] , [5,6,7])









