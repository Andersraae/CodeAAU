import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1/2, -1 , 1/2],
            [-5/2, 4, -3/2],
            [3,-3, 1]])

b = np.array([8, -28, 24])

print("Matrix : {} ".format(A))

M = np.linalg.solve(A, b)

print('Tal: ' + str(round(M[0], 2)) + ' ' + str(round(M[1], 2)) + ' ' + str(round(M[2], 2)))

