import numpy as np
import scipy
'''
Problem 3.2
a) Generate a vector x from 0 to 2π using linspace, and find the sine at each point in vector x
'''

x1 = np.linspace(0, 2 * np.pi, 50, True, False, float) # generates a vector with 50 values from 0 to 2pi
sin_x1 = np.sin(x1) # generates a vector that contains the sine at each point in vector x
# print("----------------------------------------------------------------")
# print(x1)
# print(sin_x1)


'''
b) Find the value of e^(ix) for each value in vector x, then check the magnitude of each value found.
'''
euler_x1 = np.exp(1j * x1) # finds exponential of i times x1
euler_x1 = np.abs(euler_x1) # finds magnitude of euler_x1
# print("----------------------------------------------------------------")
# print(euler_x1)


'''
c) Generate values of f(x) = x^2 + 2x + 4 using values from vector x
Numerically evaluate the integrals of f(x) and sin(x) from 0 to 2pi using scipy's cumtrapz
Compute the difference between the numerical solution to the integral from 0 to 2pi for f(x) and the analytic solution
'''
function_x1 = np.power(x1, 2) + np.multiply(x1, 2) + 4 # generates values of f(x) = x^2 + 2x + 4 using vector x
# print("----------------------------------------------------------------")
# print(x1)
# print(function_x1)

cumtrapz_sin_x1 = scipy.integrate.cumulative_trapezoid(sin_x1, x1, initial=0)
# print("----------------------------------------------------------------")
# print(cumtrapz_sin_x1[-1]) # integral of sin(x) from 0 to 2pi should logically be 0

cumtrapz_function_c1 = scipy.integrate.cumulative_trapezoid(function_x1, x1, initial=0)
# print("----------------------------------------------------------------")
# print(cumtrapz_function_c1[-1])  # integral of f(x) from 0 to 2pi should be around 147.295


'''
d) Generate a matrix of 20x20 normally distributed values with zero mean and unit standard deviation
Add I20, the 20x20 identity matrix to the result
'''
rng = np.random.default_rng() # docs https://numpy.org/doc/stable/reference/random/index.html#random-quick-start
matrix_d = rng.standard_normal(size=(20, 20)) # standard normal generator for a 20x20 array
# print("----------------------------------------------------------------")
# print(np.mean(matrix_d)) # kind of close to 0
# print(np.std(matrix_d)) # kind of close to 1

identity_matrix = np.identity(20) # makes 20x20 identity matrix
# print("----------------------------------------------------------------")
print(identity_matrix) 
print(np.add(matrix_d, identity_matrix)) # adds matrix_d to identity matrix
# print(matrix_d)

