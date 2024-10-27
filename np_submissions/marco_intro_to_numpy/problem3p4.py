import numpy as np
import scipy
'''
Problem 3.4
a) Remove the last column, the outputs from the script -- done
'''

'''
b) Find the mean and standard deviation of each column 
(each of which represents one input)
'''
iris_arr = np.loadtxt("iris.csv", delimiter=",", dtype=str)
print(iris_arr)

sepal_length_arr = iris_arr[:, 0] # extracts the first column of the iris array, which contains the sepal lengths
sepal_length_arr = sepal_length_arr[1:] # removes the first element of the sepal length arr because it contained the string 'sepal.length'
sepal_length_arr = sepal_length_arr.astype(float) # I tried to use map for this but I couldn't understand it
sepal_length_mean = np.mean(sepal_length_arr) # calculates mean 
sepal_length_std = np.std(sepal_length_arr) # calculates standard deviation

sepal_width_arr = iris_arr[:, 1] # extracts the second column of the iris array, which contains the sepal widths
sepal_width_arr = sepal_width_arr[1:] # removes the first element of the sepal width arr because it contained the string 'sepal.width'
sepal_width_arr = sepal_width_arr.astype(float)
sepal_width_mean = np.mean(sepal_width_arr)
sepal_width_std = np.std(sepal_width_arr)
# print("----------------------------------------------------------------")
# print(sepal_width_arr)

petal_length_arr = iris_arr[:, 2] # extracts the third column of the iris array, which contains the petal lengths
petal_length_arr = petal_length_arr[1:] # removes the first element of the petal length arr because it contained the string 'petal.length'
petal_length_arr = petal_length_arr.astype(float)
petal_length_mean = np.mean(petal_length_arr)
petal_length_std = np.std(petal_length_arr)
# print("----------------------------------------------------------------")
# print(petal_length_arr)

petal_width_arr = iris_arr[:, 3] # extracts the fourth column of the iris array, which contains the petal widths
petal_width_arr = petal_width_arr[1:] # removes the first element of the petal width arr because it contained the string 'petal.width'
petal_width_arr = petal_width_arr.astype(float)
petal_width_mean = np.mean(petal_width_arr)
petal_width_std = np.std(petal_width_arr)
# print("----------------------------------------------------------------")
# print(petal_width_arr)
'''
c) Standardize the data in each column so that 
each column is zero-mean, unit variance.
'''
sepal_length_standardized = np.divide((sepal_length_arr - sepal_length_mean), sepal_length_std) # subtracts the mean from each value in sepal_length_arr, then divides it by the standard deviation of the original sepal_length_arr
# print("----------------------------------------------------------------")
# print(sepal_length_standardized)

sepal_width_standardized = np.divide((sepal_width_arr - sepal_width_mean), sepal_width_std) # subtracts the mean from each value in sepal_width_arr, then divides it by the standard deviation of the original sepal_width_arr
# print("---------------------")
# print(sepal_width_standardized)

petal_length_standardized = np.divide((petal_length_arr - petal_length_mean), petal_length_std) # subtracts the mean from each value in petal_length_arr, then divides it by the standard deviation of the original petal_length_arr
# print("----------------------------------------------------------------")
# print(petal_length_standardized)

petal_width_standardized = np.divide((petal_width_arr - petal_width_mean), petal_width_std) # subtracts the mean from each value in petal_width_arr, then divides it by the standard deviation of the original petal_width_arr
# print("----------------------------------------------------------------")
# print(petal_width_standardized)
'''
d) Find the correlation matrix for the inputs 
based on the standardized matrix
(look up correlation matrix)
'''

# combining all the columns using column stack
iris_arr_standardized = np.column_stack((sepal_length_standardized, sepal_width_standardized, petal_length_standardized, petal_length_standardized))
print("----------------------------------------------------------------")
print(iris_arr_standardized)

# finds the correlation matrix for the inputs using corrcoef
iris_arr_correlation = np.corrcoef(iris_arr_standardized)
print("----------------------------------------------------------------")
print(iris_arr_correlation) # I notice it prints out in the terminal weirdly because of the matrix size, but I don't know how to reformat it
print("----------------------------------------------------------------")
print(np.round(iris_arr_correlation, 5)) # I tried to reformat it by rounding it but the matrix is still to long to be printed


