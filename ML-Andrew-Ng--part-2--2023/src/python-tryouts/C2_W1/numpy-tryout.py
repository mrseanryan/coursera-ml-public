import numpy as np

print("Array of 2:")
print("np.array([200, 13])")
print(np.array([200, 13]))
print("")

print("1 x 2 matrix (a row vector):")
print("np.array([[200, 13]])")
print(np.array([[200, 13]]))
print("")

print("2 x 3 matrix:")
print("np.array([[1,2,3], [4,5,6]])")
print(np.array([[1,2,3], [4,5,6]]))
print("")

print("2 x 1 matrix (a column vector):")
print("np.array([[200], [13]])")
print(np.array([[200], [13]]))
print("")

print("Matrix multiplication")
A = np.array([[1,-1,0.1],
            [2,-2, 0.2]
            ]) # 2 x 4 matrix
AT = A.T # transpose - 4 x 2 matrix
W = np.array([
    [3, 5, 7, 9],
    [4, 6, 8, 0]
]) # 2 x 4 matrix

print(np.matmul(AT, W))

