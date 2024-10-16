import numpy as np
from scipy.integrate import cumulative_trapezoid as cumtrapz
import matplotlib.pyplot as plt

# 1- Vector and Matrix Generation

print("Part 1: Vector and Matrix Generation\n")
v_1 = 2 * np.arange(1,17)
print(v_1)
v_2 = np.linspace(2,32,16)
print(v_2)
A = np.reshape(v_2, (4,4))
print(A)
first_row = A[0,:] # Note that python is zero-indexed!
third_column = A[:,2]
print(first_row)
print(third_column)

# 2- Fun with Functions
print("Part 2: Fun with Functions\n")
x = np.linspace(0, 2*np.pi)
sinx = np.sin(x)
plt.figure()
plt.plot(x, sinx)
plt.show()
i = np.array([1j])
euler = np.abs(np.exp(i * x))
print(euler) # All of these should equal 1- |e^(ix)| = 1 for any x!
fx = np.power(x,2) + x + 4
sin_integral = cumtrapz(sinx, x)
f_integral = cumtrapz(fx, x)
print(sin_integral)
print("Analytical answer: " + str(8*(np.pi**3)/3 + 2 * np.pi**2 + 8*np.pi))
print("Numerical approximation: " + str(f_integral[-1])) # Indexing using a negative number will fetch the nth to last element!

R = np.random.randn(20,20) + np.eye(20)
print(R)

# 3 - A Movie I Haven't Seen
print("Part 3: A Movie I Haven't Seen\n")
A = np.array([[3, -1, 4], [-1, 5, 9], [2, 6, -5]])
B = np.array([[-4], [4], [46]])
print(A)
print(B)
x = np.linalg.solve(A,B)
print(x)

# 4 - Dataset Analysis
print("Part 4: Dataset Analysis")
dataset = np.loadtxt("iris.data", delimiter=",")
dataset = np.reshape(dataset, newshape=(-1, 5))
dataset = dataset[:,0:4] # Remove last column which is just output labels

dataset = np.divide(
    dataset - np.mean(dataset, axis=0),
    np.sqrt(np.var(dataset, axis=0)),
)
print(dataset)
corr_X = dataset.T @ dataset / len(dataset)
print(corr_X)