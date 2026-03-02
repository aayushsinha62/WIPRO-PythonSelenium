import numpy as np

# reshape
a = np.arange(1,7)
print("Original array", a)

# reshape the array
reshaped = a.reshape(2, 3)
print(reshaped)


# flat = return 1D iterator over the array
arr = np.array([[1,2], [3,4]])
for x in arr.flat:
    print(x)


# flatten - Returns a copy of the array collapsed into one dimension.
arr = np.array([[1,2], [3,4]])
print(arr)

at_arr = arr.flatten()
print(at_arr)

# ravel() - Returns a flattened array
arr = np.array([[1,2],[3,4]])
print(arr)

at_arr = arr.ravel()
print(at_arr)


# pad() - Returns a padded array with shape increased according to pad_width.
arr = np.array([1,2,3])

padded = np.pad(arr, pad_width=3, mode='constant')
print(padded)

''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

#2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1 ,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanges two axes of an array.
#Axis 0 and Axis 2 swapped.
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0 , 2)
print(new_arr)
# (4 3, 2)

#moveaxis() - Moves specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)

# (3 ,4 2)

# Joining Arrays
# concatenate() - joining 2 arrays

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.concatenate((a,b), axis=0))
print(np.concatenate((a,b), axis=1))


# stack - join the arrays along the new axis
# Adds a new dimension
# All arrays must have the same shape

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.stack((a,b), axis=0))
print(np.stack((a,b), axis=1))


# hstack - Stacks arrays horizontally (column-wise).

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.hstack((a,b)))
print(np.concatenate((a,b), axis=1))


# vstack() - Stacks arrays vertically (row-wise).

print(np.vstack((a,b)))
print(np.concatenate((a,b), axis=0))


# column_stack() - Stacks 1D arrays as columns into a 2D array.
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.column_stack((a,b)))

# row_stack() - Stacks arrays row-wise.

print(np.vstack((a,b)))

# Splitting Arrays

# split arrays into multiple sub-arrays based on axis.
# Array must be divisible equally
arr = np.array([1,2,3,4,5,6])

result = np.split(arr, 3)
print(result)


# hsplit() - Splits array horizontally (column-wise)
# Works on 2D arrays.

arr2 = np.array([[1,2,3,4],
                 [5,6,7,8]])

print(np.hsplit(arr2, 2))


# vsplit() - Splits array vertically (row-wise)

arr2 = np.array([[1,2],
                 [3,4],
                 [5,6],
                 [7,8]])

print(np.vsplit(arr2, indices_or_sections=2))

# array_split() - Similar to split(), but does NOT require equal division.

arr = np.array([1,2,3,4,5])

print(np.array_split(arr, indices_or_sections=3))

# Adding / Removing Elements

# resize() - Returns a new array with a specified shape.

arr = np.array([1,2,3,4])
new_arr = np.resize(arr, new_shape=(2,3))
print(new_arr)

# the elements will repeat in the new array
# returns a new array


# append() - Appends values at the end of an array.

arr = np.array([1,2,3])
new_arr = np.append(arr, values=[4,5])
print(new_arr)


# 2D array
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
np.append(a, b, axis=0)

# Repeating
# repeat() is used to repeat each element of an array a specified number of times.
# Each element is repeated twice.
arr = np.array([1, 2, 3])
print(np.repeat(arr, repeats=3))


# Different Repeats for Each Element
arr = np.array([10, 20, 30])
print(np.repeat(arr, repeats=[1, 2, 3]))


# Repeat in 2D Array
arr2 = np.array([[1,2],
                 [3,4]])

print(np.repeat(arr2, repeats=2, axis=0))


# tile() The input array that will be repeated.
my_array = np.array([1, 2, 3])
tiled_array = np.tile(my_array, reps=2)

print("Original Array:", my_array)
print("Tiled Array:", tiled_array)

# Rearranging Elements
# flip() - Reverses the order of elements along a given axis.

# If axis=None → reverses entire flattened array
# If axis=0 → reverse rows
# If axis=1 → reverse columns

arr = np.array([1,2,3,4])
print(np.flip(arr))

# 2D
arr2 = np.array([[1,2],
                 [3,4]])

print(np.flip(arr2, axis=0))   # Flip rows
print(np.flip(arr2, axis=1))   # Flip columns


# fliplr() - Flip Left-Right (axis=1) - Works only on 2D+ arrays.

arr2 = np.array([[1,2,3],
                 [4,5,6]])
print(np.fliplr(arr2))

# flipud - Flip Up-Down (axis=0)

print(np.flipud(arr2))


# roll() - Rolls (rotates) elements along a given axis.

arr2 = np.array([[1,2,3],
                 [4,5,6]])

np.roll(arr2, shift=2, axis=None)

# sort() Returns a sorted copy of an array (or sorts in-place if using ndarray method)

arr = np.array([5, 2, 9, 1])
sorted_arr = np.sort(arr)

print(sorted_arr)

# argsort() - Returns the indices that would sort the array return the index positions
arr = np.array([5, 2, 9, 1])
sorted_arr = np.sort(arr)
print(sorted_arr)

indices = np.argsort(arr)
print(indices)


# lexsort() - Used for sorting with multiple columns (like sorting by last name, then first)
# Sort by a first
# then by b (secondary key)
# Sorting happens from right -> left.

a = np.array([1, 1, 0, 0])
b = np.array([1, 0, 1, 0])

result = np.lexsort((b, a))
print(result)