import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 8 * x**2 + (-28) * x + 24

x = np.linspace(0,4,100) # x start, y start, amount of points

plt.plot(x, f(x), color='red', label='Polynomial')

xes = np.array([1, 2, 3])
ys = np.array([4, 0 , 12])

plt.plot(xes, ys, '*', label='Datapoints')

plt.grid(True)
plt.legend()

# show the plot
plt.show()