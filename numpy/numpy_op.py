import numpy as np
array=np.array([1,2,3,4,5,6,7])
#numpy array
print(type(array))
#multi_dimensional_array
multi_dimensional_array=np.array([[1,2,3],[4,5,6]])
print((multi_dimensional_array))
#no of rows and columns in multi_dimensional_array
print(multi_dimensional_array.shape)

#creating and intializing arrays with random numbers
zero_array=np.zeros((5,5),dtype=int)
print(zero_array,"\n")
specific_no_array=np.full((5,5),2,dtype=int)
print(specific_no_array,"\n")
random_array=np.random.random((3,4))
print(random_array,"\n")
ones_array=np.ones((5,5),dtype=int)
print(ones_array,"\n")

#accesing specific values
print(ones_array[0,2])
#check which values are greater tan 0.2
print(random_array > 0.2)
#returns values greater than 0.2
print(random_array[random_array>0.2])
#sum of the useful numpy functions
print(np.floor(ones_array))