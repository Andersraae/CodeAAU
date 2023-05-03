import numpy as np

A = np.array([[1,1,0,0],
              [0,0,1,1],
              [1,0,1,0],
              [0,1,0,1],
              [0,1,0,0],
              [1,0,0,1],
              [0,0,1,0],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,1]],
             dtype=np.double)

print("A=", A)

b = np.array([[1],
              [5.25],
              [2],
              [3.5],
              [1.5],
              [3],
              [1.75],
              [0],
              [2.5],
              [3]])

print('b = ', b)

# Compute the QR factorization
Q,R = np.linalg.qr(A)

print('QR factorization')
print("Q=", Q)
print("R=", R)
# Note that Q^T Q ~ I, up to some small round-offs
# i.e. Q is an orthogonal matrix
print("Q^T Q = ", Q.T @ Q)
print("Q R = ", Q @ R)

Rpx = Q.T @ b

print('QT . b = ', Rpx)

x = np.linalg.solve(R, Rpx)

print('x = ', x)

print()
print('least squares solustion b hat = ', A @ x)
print('b = ', b)


z = b - (A @ x)

zNorm = np.linalg.norm(z)

print()
print('z = b - b hat =  ', z)
print('||z|| = ', zNorm)

print()
print()
print()

print('Least squares solution with normal equations')

print('AT = ', A.T)
print('inverse(AT.A) = ', np.linalg.inv(A.T @ A))

xHat = np.linalg.inv(A.T @ A) @ A.T @ b
print('x hat = ', xHat)

bHat = A @ xHat
print('b hat = ', bHat)

z2Norm = np.linalg.norm(b - bHat)
print('z = ', b - bHat)
print('norm(z) = ', z2Norm)

Az = np.array([[1,1,0,0, 0.04761905],
              [0,0,1,1, 0.38095238],
              [1,0,1,0, 0.04761905],
              [0,1,0,1, -0.36904762],
              [0,1,0,0, 0.60714286],
              [1,0,0,1, -0.03571429],
              [0,0,1,0, -0.14285714],
              [1,0,0,0, -0.05952381],
              [0,1,1,0, -0.28571429],
              [0,0,0,1, 0.02380952]],
             dtype=np.double)

print("Az=", Az)