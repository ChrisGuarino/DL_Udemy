#Panda Series is build right on top of a Numpy array. 
#It has a named Index as opposed to a number. 
"""
import numpy as np 
import pandas as pd 

labels = ['a','b','c']
mylist = [10,20,30]

arr = np.array(mylist) 

d = {'a':10,'b':20,'c':30}

#Pass in raw data into Pandas Series
print(pd.Series(data=mylist)) 

#Now lets use the index field in the Series 
print(pd.Series(data=mylist,index=labels)) 

#Data does not need to be nummerical 

ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
print(ser1) 

#You can still use the labels and data to call eachother. 
print(ser1['USA']) 

#Pandas can perform opertions on multiple Series 
ser2 = pd.Series([5,6,7,8],['USA','Germany','Italy','Japan'])
print(ser1 +ser2)  
""" 

#Dataframe - like a data table 
#A Dataframe is more than one Series that share one index

import pandas as pd 
import numpy as np 
from numpy.random import randn 

#Dummy Data
np.random.seed(101)
rand_mat = randn(5,4) 

df = pd.DataFrame(data=rand_mat,index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)  

#Single Column 
print(df['W'])

#More than one Column 
mylist = ['W','Y']
print(df[mylist])

#Create a new Column 
df['New'] = df['W'] + df['Y'] 
print(df) 

#To remove a column, this also works for rows. Just remove the "axis" arguement. Sets default to 0. Keep in mind you won't need the axis=1. This is not presistent. 
df.drop('New',axis=1)
#If you want it to be presistent you add "inplace=True" argument 

#Access a single Row 
print("Row:\n",df.loc['A']) 
#You can also use the numpy index location instead of the Pandas label 
print("Row:\n",df.iloc[0])

#Select mutliple rows 
print("Multiple Row\n", df.loc[['A','E']]) #For mutliples you just need to pass in a list of rows. 

#Select Multiple Columns 
print("Mutliple Columns:\n",df.loc[['A','B'],['Y','Z']])#Use multiple lists. Rows then columns


#Conditional Selection 
print(df>0) 
df_bool = df >0 

#We can now pass this into our dataframe and it will give us only the fields that return True. 
print("Conditional Selection:\n", df[df_bool]) #Passing a filtered row into the dataframe. Only return the values that mett the condition.
print("Conditional Filtering:\n", df[df['W']>0]) #More common way of seeing this

#Filtering the dataframe for conditions 
print("Conditional Filtering:\n",df['W']>0)  

#You can stack the operations. This gives the ability to select specific data from a dataframe. 
print("Operations Stacking:\n",df[df['W']>0]['Y'].loc['A']) 

#Two Coniditions or More 
cond_1 = df['W']>0
cond_2 = df['Y']>1



