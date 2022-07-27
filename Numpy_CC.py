""" import numpy as np 

mylist = [1,2,3]
print(type(mylist)) 

#Convert python list to Numpy array
arr = np.array(mylist)
print(arr) 
print(arr.shape)

#Transfering a nested list or matrix into numpy array. 
mymatrix = [[1,2,3], [4,5,6], [7,8,9]] 
print(mymatrix)

#Convert to Numpy Array 
arr_mat = np.array(mymatrix) 
print(arr_mat)

#Get the shape of the matrix. 
print(arr_mat.shape) 

#Generate a new array in range
print(np.arange(0,10))

#Generate 0's and 1's 
print(np.zeros((4,10)))
print(np.ones((5,10))+4)

#Cool thing about Numpy arrays is that you can perform maths operations on it. 
#Broadcast arithmatic across the entire array. 

#Create linearly spaced arrays. 
#Give a range and how many evenly space numbers you want in that range. 
print(np.linspace(0,10,3))

#Create an identity matrix 
print(np.eye(5)) 

#Creating random numbers. 

#Give a random sample between 0 and 1. 
#Uniform distribution - Planar shape
print(np.random.rand(4,3)) 

#Normal distribution - Bell shaped
print(np.random.randn(10))

#Specify Mean and Sigma 
np.random.normal() 

#Random Ingeters in Range 
print(np.random.randint(1,100,10))

#You can set a Seed to get the same set of random numbers over and over. 
np.random.seed(42)
print(np.random.rand(4)) 

#Array Attributes and Methods 
arr = np.arange(25)
print(arr) 

ranarr = np.random.randint(0,50,10)
print(ranarr)

#Reshaping Array
print(arr.reshape(5,5))  

#Max and Min of Array 
print(ranarr.max(),'\n',ranarr.min())

#Max and Min Index Positions 
print(ranarr.argmax())
print(ranarr.argmin())

""" 
"""
import numpy as np 

#Indexing
arr = np.arange(0,11) 
print(arr[10])

#Slicing - These still point to the original array. 
print(arr[1:7]) 

#Broadcasting - This is what makes them special from normal Python Lists
#This happens in place so if you want the operation to be presistent you need to assign the change to a varibable. 
print(arr+100) 
print(arr/2)

#If you didnt want any of your opertations to effect your original array you use a copy. 
#Makes a distinct copy of the array in memory. 
arr_copy = arr.copy() 
arr_copy[:] = 1000 
print("New: ",arr_copy,"\nOld: ",arr)  

#Indexing on a 2D array - Matrix 
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
print(arr_2d[:2,1:]) 

#Comparision Opertaions 
arr = np.arange(1,11) 
print(arr>4) 

#You can use comparison to make a boolean object and pass it's boolean values into your original array for index selection. 
#It is looking for the "True" values to return on each index. 
bool_arr = arr>4 
print(arr[bool_arr])

#To make this syntax easier 
arr[arr>4] #Does the same thing as the above. 
"""
"""
import numpy as np 

arr = np.arange(0,10)

#You can perform aritmatic of two arrays. 
print(arr*arr)

#Math Functions - Tons of them loop them up when you need them
print(np.sqrt(arr))

#Mean, Min, Max  - Many of them look up
print(arr.sum())  

arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(arr_2d.sum()) #Just sums all the numbers. 

#Gives the sum across the rows.
print(arr_2d.sum(axis=0)) 

#Or across the columns. 
print(arr_2d.sum(axis=1))
""" 
#EXERCISES
from textwrap import indent
import numpy as np 

arr_zeros = np.zeros(10) 
arr_ones = np.ones(10) 
arr_fives = np.ones(10)*5

arr_1 = np.arange(10,51) 
print(arr_1)

arr_even = arr_1[arr_1%2==0] 
print("Evens:\n",arr_even)

mat_three = np.array([[0,1,2],[3,4,5],[6,7,8]]) 
print("3 x 3 Matrix:\n",mat_three) 

ident_mat = np.eye(3) 
print("Identity Matrix:\n",ident_mat) 

random_num = np.random.rand() 
print(random_num) 

random_num = np.random.randn(25) 
print(random_num) 

arr_hundred = np.linspace(0.01,1,100) 
print(arr_hundred)

arr_twenty = np.linspace(0,1,20) 
print(arr_twenty) 

mat = np.arange(1,26).reshape(5,5)
print("To be Sliced:\n",mat)

sliced = mat[2:,1:] 
print("Sliced:\n",sliced) 

sliced = mat[3,4]
print("Sliced:\n",sliced) 

sliced = mat[:3,1:2]
print("Sliced:\n",sliced) 

sliced = mat[4]
print("Sliced:\n",sliced) 

sliced = mat[3:] 
print("Sliced:\n",sliced) 

sum_mat = mat.sum() 
print("Sum:\n",sum_mat) 

stdev_mat = np.std(mat) 
print("Standard Deviation:\n",stdev_mat) 

sum_columns = mat.sum(axis=0)
print("Sum of all the rows:\n",sum_columns) 

np.random.seed(42)