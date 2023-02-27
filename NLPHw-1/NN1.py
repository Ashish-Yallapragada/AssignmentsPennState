import numpy as np

data = np.loadtxt('data.txt')
X = data[:, :-1]
Y = data[:, -1:]
X = np.column_stack((np.ones_like(X), X))
# Separate X and Y data

print(X)
print(Y)
# Calculate X'X and its inverse
XtX = np.dot(X.T, X)
XtX_inv = np.linalg.inv(XtX)

# Calculate X'Y
XtY = np.dot(X.T, Y)

# Calculate regression coefficients b
b = np.dot(XtX_inv, XtY)

# Output results
print("X:\n", X)
print("X'X:\n", XtX)
print("(X'X)^-1:\n", XtX_inv)
print("X'Y:\n", XtY)
print("b:\n", b)
