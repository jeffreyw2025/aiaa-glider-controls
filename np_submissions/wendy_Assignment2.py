import numpy as np
from scipy.integrate import cumulative_trapezoid as cumtrapz
import matplotlib.pyplot as plt

#qs1, python range function to index 2 to 32 using range
print("\nVector and Matrix Generation\n")

#use range
list1 = list(range(2, 33, 2))
#use linspace
even_number = np.linspace(2,32,16,dtype=int)

#rearrange array and put into matrix, print
matrix = even_number.reshape((4,4))
print("The matrix is\n", matrix)

#extract ftn
def extract_row(matrix,index, is_row=True):
    if(is_row):
        #specific row
        return matrix[index, :]
    else:
        #specific column
        return matrix[:,index]

row1 = extract_row(matrix,0, is_row=True)
column3 = extract_row(matrix, 2, is_row=False)

print("\nFor row 1\n", row1)
print("\nFor column 3\n", column3)


#qs2, fun with ftns 
print("\nFun with Function\n")

#a. sin of vector from 0 to 2pi
x = np.linspace(0, 2*np.pi)
sinftn = np.sin(x)

#b. Find e^ix(i->1j), check magnitude 
exponential = np.exp(1j*x)
magnitude = np.abs(exponential)
print("The magnitude for e^ix is\n", magnitude)

#c. f(x) and cumtrapz ftn
fx = pow(x,2) + 2*x + 4
integral_sinx = cumtrapz(sinftn, x)
integral_fx = cumtrapz(fx, x)
print("Analytic result:", 8*pow(np.pi,3)/3 + 2*pow(np.pi,2)+8*np.pi)
print("Numerical result:", integral_fx[-1])

#d. Generate matrix and add identity matrix
mtx = np.random.normal(size=(20,20))
idtmtx = np.identity(20) #can also use np.eye()
rlt = np.add(mtx, idtmtx)
print("\nResult matrix:\n", rlt)


#qs3 A movie I haven't seen A^-1b
print("\nA movie I haven't seen")

A = np.array([[3,-1,4], [-1,5,9], [2,6,-5]])
b = np.array([[-4], [4], [46]])
Ainverse = np.linalg.inv(A)
sln = np.dot(Ainverse,b)    #dot prodect
print("The solution to the system of equation is:\n", sln)


#qs4 Dataset Analysis
print("\nDataset Analysis")

#part a. Include iris.csv file in local repository
irisdata = np.loadtxt('iris.csv', dtype = str, delimiter=',')
iris_new = np.delete(irisdata, -1, 1)         #remove last column(-1), delete along column(1)
iris_float = iris_new.astype(float)           #put into float array

#part b. Mean and standard deviation along each column
iris_means = np.mean(iris_float, 0)
iris_std = np.std(iris_float, 0)
print("Mean of iris data is:\n", iris_means,"\n")
print("Standard deviation of iris data is\n", iris_std, "\n")

#part c.  Standardize the data
iris_stdize = np.divide(iris_float - iris_means, iris_std)
print("Standarized iris data:\n", iris_stdize, "\n")

#part d. Correlation Matrix
iris_correlation = np.corrcoef(iris_stdize, rowvar= False)
print("Correlation Matrix is:\n", iris_correlation)