import numpy as np

# Read data from text file
data = np.loadtxt('data.txt')

# Separate X and Y data
Y = data[:, :1]
X = data[:, 1:]

# Add column of ones to X for the intercept term
X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)

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
