import numpy as np

# Creating a NumPy Array using a list.
num1d = np.array([1,2,3,4,5,6]) # 1d Array
num2d = np.array([[1,2],[3,4],[5,6]]) # 2d Array

print(num1d)
print(num2d)


# Array Attributes
print(num1d.shape) # Shape of the Array
print(num2d.ndim) # Number of Dimensions
print(num2d.size) # Number of Elements


# Basic Operations
array = np.array([10,20,30])
print(array)
increasedArray = array + 5 # add 5 to each element
print(increasedArray)


# Mathematical Functions
mean = np.mean(array)
stdDev = np.std(array) # Standard Deviation


# Indexing and Slicing
firstElement = array[0]
subArray = array[1:3] # Index from 1 to 2

print(firstElement)
print(subArray)