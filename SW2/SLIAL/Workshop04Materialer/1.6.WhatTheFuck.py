import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,1,-1,-1,1,0,0,-1,0,0],
              [1,3,-1,-3,0,1,0,0,-1,0],
              [1,6,-1,-6,0,0,1,0,0,-1]],
             dtype=np.double)


y = np.array([[-1],
              [-1],
              [-1]])


print(A.T.dot(y))


