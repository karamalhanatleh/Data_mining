# Python Pandas Tutorial 2: Dataframe Basics:
# https://www.youtube.com/watch?v=F6kmIpWWEdU
'''
Pandas
Pandas is a key Python library for data scientists. It has a data structure
called DataFrame which is like a table of data.
With Pandas we can read csv/xls files, store and manipulate the data in DataFrames.

'''
import pandas as pd
import numpy as np

emp = {'name':['Ahmed', 'Sarah', 'Ali', 'Noora', 'Amro'],
       'age':[28, 32, 25, 19, 30],
       'salary':[1000, 1500, 800, 500, np.nan]}
emp_df = pd.DataFrame(emp)
print(emp_df)
#print()
# printing dimensions and columns names
print("DF shape: ", emp_df.shape)
print("DF columns: ", emp_df.columns)

#getting descriptive statistics of numeric columns in data
print(emp_df.describe())

# getting number of null values in each columns
print()
print(emp_df.isna().sum())
emp_df.dropna(inplace=True) # drop all rows with any null value
print(emp_df)

print(emp_df.query('salary >= 1000')) # Query the frame
print(emp_df.loc[emp_df['age'] == 25]) # Filter the frame
print(emp_df)
#########################################################
# save it to csv:
emp_df.to_csv('emp_data.csv', index = False)

# read fromthe csv:
saved_df = pd.read_csv('emp_data.csv')
#print(saved_df.head(2))


#########################################################

################## RANDOM nps matplotlib #####################
import matplotlib.pyplot as plt
plt.scatter(saved_df.age, saved_df.salary)
plt.title('Display Data')
# Add an X & Y Label
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

