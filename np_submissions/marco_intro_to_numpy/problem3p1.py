import numpy as np
import scipy
# Marco Chen
# Note: Sorry for my messy coding style, I have coded very little in python before and I will try to be more concise with my comments in the next assignments
'''
Problem 3.1:
Generate a vector of even numbers from 2 to 32 (inclusive) using both indexing and linspace. Then
reshape the vector into a 4x4 matrix, with elements going left to right then up to down. Finally,
extract the first row and the third column from the 4x4 matrix you generate.
'''

x1 = np.linspace(2, 32, 31, True, False, int) # I am generating integers because I don't know how to classify floats as even or odd
even_x1 = x1[x1 % 2 == 0] # only keep values of x1 that are even
matrix_x1 = even_x1.reshape(4, 4) # reshapes x1 into a 4x4 matrix
matrix_x1_row1 = matrix_x1[0, :] # extracts the first row of matrix_x1
matrix_x1_col3 = matrix_x1[:, 2] # extracts the third column of matrix_x1
print("----------------------")
print(x1)
print("----------------------")
print(even_x1)
print("----------------------")
print(matrix_x1)
print("----------------------")
print(matrix_x1_row1)
print("----------------------")
print(matrix_x1_col3)
