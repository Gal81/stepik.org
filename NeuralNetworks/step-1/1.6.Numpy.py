import numpy as np
from urllib.request import urlopen

# matrix = np.array([[2,1,0,0], [0,2,1,0], [0,0,2,1]], dtype=float)
# matrix = matrix.reshape((12,1))
# print(matrix)

# x_shape = tuple(map(int, '2 3'.split()))
# X = np.fromiter(map(int, '8 7 7 14 4 6'.split()), int).reshape(x_shape)

# y_shape = tuple(map(int, '4 3'.split()))
# Y = np.fromiter(map(int, '5 5 1 5 2 6 3 3 9 1 4 6'.split()), int).reshape(y_shape)

# try:
#     Z = X.dot(Y.transpose())
#     print(Z)
# except:
#     print('matrix shapes do not match')

url = 'https://stepic.org/media/attachments/lesson/16462/boston_houses.csv'
data = urlopen(url)
matrix = np.loadtxt(data, skiprows=1, delimiter=",", dtype=float)
print(matrix.mean(axis=0))

