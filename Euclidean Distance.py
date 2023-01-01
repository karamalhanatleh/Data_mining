# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:24:27 2022

@author: Karam Alhanatlh
"""
import math
def Euclidean_distance(x2,x1 , y2,y1):
    eun_dis=  math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return "Euclidean Distance : " ,eun_dis

print(Euclidean_distance(1,4,2,5))