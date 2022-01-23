import numpy as np

# 1.7.3
# arr = ((0, -0.5), (1, 0), (0, 0.5), (0, 1.5), (1, 2.5), (2,3))

# def sqerr(a, b):
#   return (a - b)**2

# def abserr(a, b):
#   return abs(a - b)

# def errsum(err_fun):
#   return sum(list(map(lambda pair: err_fun(pair[0], pair[1]), arr)))

# print(str(max(errsum(abserr), errsum(sqerr))))
# print(str(errsum(sqerr)))
# print(str(errsum(abserr)))

# 1.7.5
X = np.array([[1,60], [1,50], [1,75]], dtype=float)
Y = np.array([[10], [7], [12]], dtype=float)
step1 = X.T.dot(X)
step2 = np.linalg.inv(step1)
step3 = step2.dot(X.T)
b = step3.dot(Y)
print(b)