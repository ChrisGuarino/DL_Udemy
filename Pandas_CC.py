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

#Creat a new Column 
df['New'] = df['W'] + df['Y'] 
print(df) 

#To remove a column, this also works for rows. Keep in mind you won't need the axis=1. 
df.drop('New',axis=1)