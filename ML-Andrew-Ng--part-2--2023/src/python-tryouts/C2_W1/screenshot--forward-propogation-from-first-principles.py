import numpy as np

print("see screenshot--forward-propogation-from-first-principles.jpg")

# open ../../images/screenshot--forward-propogation-from-first-principles.jpg

# a_in - the input (X if 1st layer 0)
# W - weights - same dims as X
# b - constant
#
# g - activation function - can be sigmoid.  for images, could be ReLU.

def g(Z):
    return Z

# sets up one layer (list of nodes)
def dense(a_in, W, b):
    units = W.shape[1]
    a_out = np.zeros(units)
    for j in range(units):
        w = W[:,j]
        z = np.dot(w, a_in) + b[j]
        a_out[j] = g(z)
    return a_out

# much more efficient than for loops, due to hardware optimizations
def dense_via_vectorization(A_in, W, b):
    AT = A_in.T # transpose
    Z = np.matmul(AT, W) + b # works if dimensions match: A_in is M x N and W is N x O and B is O
    A_out = g(Z)
    return A_out

X = np.array([[200,17]]) # 1 x 2 matrix. so W needs to be 2 x N so can dot product, where N is number of nodes

W1 = np.array([[1, -3, 5], [2,4,-6]]) # randomly initialised, then learned in training
W2 = W1 # TODO - Captial letter = a Matrix (lower case is a vector or scalar).
W3 = W2 # TODO
W4 = W3 # TODO

b1 = 0.3
b2 = b1 # TODO
b3 = b2 # TODO
b4 = b3 # TODO

# set up a set of layers (a neural net)
def sequential(x):
    a1 = dense(x, W1, b1)
    a2 = dense(a1, W2, b2)
    a3 = dense(a2, W3, b3)
    a4 = dense(a3, W4, b4)
    f_x = a4
    return f_x
