from operator import eq
from sympy.abc import a
import numpy as np
from sympy import *
from scipy.linalg import lu, lu_solve, lu_factor
from time import time

# code matrices A and b

A = np.array([[0.4586, 0.5075, 0.4714], [0.7572, 0.8071, 0.8376],
              [1.0324, 0.9737, 0.8904]])
B = np.array([0.0414, 0.0988, 0.2007])

# Solve the linear system get the three unknowns : x, y , z

X = np.linalg.solve(A, B)
# X = np.linalg.inv(A).dot(B)
print(X)


# CONFIRMING WHETHER OUR UNKNOWNS ARE CORRECT
x = X[0]

y = X[1]

z = X[2]
U = 0.4586*X[0] + 0.5075 *X[1] + 0.4714*X[2]
S = 0.7572*X[0] + 0.8071 *X[1] + 0.8376*X[2]
T = 1.0324*X[0] + 0.9737 *X[1] + 0.8904*X[2]
print(U)
print(S)
print(T)


# Finding a formulae of the well-being of the validation data


print('Enter the income , idi , education and well-being respectively:')
x = float(input())
y = float(input())
z = float(input())
R = float(input())
Q = (x*X[0] + y *X[1] + z*X[2])/10
print('The approximated well-being is ', Q)

# Calculating the error in approximation
E = (R-Q)
print('The error in approximation is ', E)


