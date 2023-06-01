import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,1],
              [1,3],
              [1,6]],
             dtype=np.double)

print("A=", A)

b = np.array([[-10],
              [30],
              [60]])

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

print()
print('Q.T @ b = ', Q.T, '@', b)
Rpx = Q.T @ b

print('QT . b = ', Rpx)

x = np.linalg.solve(R, Rpx)

print('x = ', x)

print()
print('least squares solustion b hat = ', A @ x)
print('b = ', b)
print()
print()

def f(x):
    return -18.94736842 + 13.68421053 * x

x = np.linspace(0,8,100) # x start, y start, amount of points

plt.plot(x, f(x), color='red', label='Polynomial')

xes = np.array([1, 3, 6])
ys = np.array([-10, 30 , 60])

plt.plot(xes, ys, '*', label='Datapoints')

plt.grid(True)
plt.legend()

# show the plot
plt.show()