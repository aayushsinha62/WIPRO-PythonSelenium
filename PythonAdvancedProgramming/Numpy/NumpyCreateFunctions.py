import numpy as np


# '''
#     Using numpy.array() Function
#     Using numpy.zeros() Function
#     Using numpy.ones() Function
#     Using numpy.arange() Function
#     Using numpy.linspace() Function
#     Using numpy.random.rand() Function
#     Using numpy.empty() Function
#     Using numpy.full() Function
# '''


# This function creates a NumPy array filled with zeros
# By default, the data type is float64
a = np.zeros(5)
print(a)

# 2D array of zeros
a_2D = np.zeros((4, 3))
print(a_2D)

# Using numpy.ones() Function
a = np.ones(5)
print(a)

# 2D array of ones
a_2D = np.ones((4, 3))
print(a_2D)


# Using numpy.arange() Function
# The numpy.arange() function creates an array by generating a sequence of numbers based on specified start, stop and step values.
# It is similar to Python's built-in range() function.

# with only the stop
a = np.arange(10)
print(a)

# providing the start, stop and step values
a = np.arange(1,  10, 2)
print(a)

# Using numpy.linespace() Function
a=np.linspace(0,10,num=5,endpoint=False)
print(a)

#includes last number
a=np.linspace(0,10,num=5,endpoint=True)
print(a)

# Using numpy.empty() Function
# 2D
# This function initializes an array without initializing its elements;
# the content of the array is arbitrary and may vary

a = np.empty((2,3))
print(a)


# Using numpy.full() Function
# In the following example, we are using the numpy.full() function to create a 2-dimensional
# array filled entirely with the value 5

a = np.full(shape=(2,3), fill_value=5)
print(a)

# numpy.eye()
# The NumPy eye() function is used to
# create a 2D array with ones on the diagonal and zeros in all other positions

identity_matrix = np.eye(4)
print(identity_matrix)


# numpy.identity - function is used generate a square identity matrix.
identity_matrix = np.identity(5)
print(identity_matrix)


# numpy.diag
# In case of 2D array, the function extracts the diagonal elements of the array.
# In case of 1D array, the function creates a square diagonal matrix with the elements
# of the diagonal values and zeros in remaining positions.

Matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Original matrix", Matrix)

Diagonal_elements = np.diag(Matrix)
print("Diagonal elements", Diagonal_elements)