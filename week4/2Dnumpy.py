import numpy as np
import matplotlib.pyplot as plt


A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])

X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]])

Z = np.dot(A, B)
print(A.T)
