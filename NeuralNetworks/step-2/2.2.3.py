import numpy as np

X = np.array([[1, 1, 1, 1]])

w1 = np.array([[0, -10, 5, 2]]).T
w2 = np.array([[-5, -1, 10, 0]]).T
w3 = np.array([[2, -1, 15, -20]]).T
w4 = np.array([[4, -1, 1, 0]]).T

print(X.dot(w1))
print(X.dot(w2))
print(X.dot(w3))
print(X.dot(w4))