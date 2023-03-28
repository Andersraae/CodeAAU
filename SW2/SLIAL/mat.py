import numpy as np

A = np.matrix([[1, 3],
              [4, 5]])

print('Determinant: ')
print(np.linalg.det(A))
print('Transpose: ')
print(np.transpose(A))
print('Inverse: ')
print(1/np.linalg.det(A) * A.getH())
print('Inverse 2: ')
print(np.linalg.inv(A))
print('1 matrix: ')
print(np.matmul((1/np.linalg.det(A) * np.transpose(A)), A))
print('1 matrix 2: ')
print(np.matmul(np.linalg.inv(A), A))
print()
print()
print(A.getH())
print(np.transpose(A))
