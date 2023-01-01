# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:03:27 2022

@author: Karam Alhanatlh
"""

#  K-Means Clustering with Python
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for statistical data visualization


import warnings
warnings.filterwarnings('ignore')



data = 'Liv.csv'
df = pd.read_csv(data)

print(df.isnull().sum())

df.drop(['Column1', 'Column2', 'Column3', 'Column4'], axis=1, inplace=True)
print("\n\n\n")
print(df.isnull().sum())


df['status_id'].unique()

df.drop(['status_id', 'status_published'], axis=1, inplace=True)

X = df

y = df['status_type']






















