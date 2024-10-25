import numpy as np
import scipy

'''
Matrix to be solved:
3x - y + 4z = -4
-x + 5y + 9z = 4
2x + 6y - 5z = 46
Let A = the coefficient matrix
Let B = the solutions of the coefficient matrix
'''
A = np.array([
    [3, -1, 4],
    [-1, 5, 9],
    [2, 6, -5]])
print(A)

B = np.array([[-4],
              [4],
              [46]])

# Let X = the solution to the system of equations
# Equation: (A^-1)dot(B) = X
# performs the operations, on line 23, on matrices A and B
X = np.dot(np.linalg.inv(A), B) # I used this youtube video https://www.youtube.com/watch?v=jTCCgxUXhW4 to figure out the dot function but I did check the documentation afterward
print(X)

# x = 3, y = 5, z = -2