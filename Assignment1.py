# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 20:26:39 2022

@author: Karam Alhanatlh
"""


#  import packages
import pandas as pd
import matplotlib.pyplot as plt
import math



#  Create DataFrame
student= pd.DataFrame({
    "Points":["p1" , "p2" , "p3" , "p4" , "p5" , "p6"],
    "X":     [1.0 , 1.0 , 2.0 , 2.0  ,3.0 , 4.0],
    "Y":     [1.5 , 4.5 , 1.5 , 3.5, 2.5, 6.0 ] ,
    
    
               }    )


#   set index it Points
student=student.set_index('Points')



###     Construct a data frame containing the data  and print  the first 4 rows
print(student.head(4))



###############

###    Scatter plot the x,y variables with title. 

fix , ax= plt.subplots()
ax.scatter(student["X"] , student["Y"]  , s=50  , marker="X" , color="red")
ax.set_xlabel(" X")
ax.set_ylabel("Y")
plt.show()

###############

###    Write a function to compute the Euclidean distance between points (p1 and p6) and then call the function 

def Euclidean_distance(x2,x1 , y2,y1):
    eun_dis=  math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return "Euclidean Distance : " ,eun_dis

print(Euclidean_distance(1,4,1.5,6))

print(Euclidean_distance(student.X[0],student.X[-1],student.Y[0], student.Y[-1]))

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    