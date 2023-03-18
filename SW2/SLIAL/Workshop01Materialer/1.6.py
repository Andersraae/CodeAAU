import numpy as np
import matplotlib.pyplot as plt

A = np.array([[0, 0, 0, 0, 1],
            [(np.pi/6)**4, (np.pi/6)**3, (np.pi/6)**2, np.pi/6, 1],
            [(np.pi/4)**4, (np.pi/4)**3, (np.pi/4)**2, np.pi/4, 1],
            [(np.pi/3)**4, (np.pi/3)**3, (np.pi/3)**2, np.pi/3, 1],
            [(np.pi/2)**4, (np.pi/2)**3, (np.pi/2)**2, np.pi/2, 1]])

b = np.array([1, np.sqrt(3)/2, np.sqrt(2)/2, 1/2, 0])

print("Matrix : {} ".format(A))

M = np.linalg.solve(A, b)

print(M)

# Plot begins

xes =np.array([0, np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2])
plt.plot(xes, b, '*', label='Datapoints')

x = np.linspace(-1, 2, 100)

def f(x):
    return 0.0288 * x**4 + 0.0234 * x**3 + (-0.5152) * x**2 + 0.0034 * x + 1

plt.plot(x, f(x), color='blue', label='Polynomial')
plt.plot(x, np.cos(x), color='red', label='Cos')

plt.grid(True)
plt.legend()

plt.show()