import numpy as np

I = np.array([[1,0,0],
              [0,1,0],
              [0,0,1]])
B = np.array([[ 3,  -3,   1. ],
             [-5/2,  4,  -3/2],
             [ 1/2, -1,   1/2]])
A = np.array([[1, 1, 1],
                [1, 2, 4],
                [1, 3, 9]])

# print(np.matrix.round(np.matmul(I, np.linalg.inv(B))))
print(np.matmul(A,B))


b = np.array([[3], [-5/2], [1/2]])

print()
print(np.dot(A,b))