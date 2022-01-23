import urllib
from urllib import request
import numpy as np

# fname = input() # read file name from stdin
# f = urllib.request.urlopen(fname) # open file from URL
# data = np.loadtxt(f, delimiter=',', skiprows=1) # load data to work with

with open('NeuralNetworks\\dump\\boston_houses.csv', 'r') as f:
    data = np.loadtxt(f, delimiter=',', skiprows=1)

XY = np.array(data, dtype=float)
Y = np.copy(XY[:, 0])
X = np.copy(XY)
X[:, 0] = 1

step1 = X.T.dot(X)
step2 = np.linalg.inv(step1)
step3 = step2.dot(X.T)
b = step3.dot(Y)

for a in b:
    print(a, end=' ')
