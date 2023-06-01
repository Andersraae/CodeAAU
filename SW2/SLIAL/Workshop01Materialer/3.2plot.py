import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return 1 * ((1-t)**3) + 3*0*t*((1-t)**2) + (3 * (3)*(t**2)*(1-t)) + (-3)*(t**3)

def y(t):
    return 1 * (1-t)**3 + 3*6*t*(1-t)**2 + (3 * (-3)*(t**2)*(1-t)) + (1)*(t**3)


t = np.linspace(1,4,100) # x start, y start, amount of points

plt.plot(t, x(t), color='red', label='x(t)')
plt.plot(t, y(t), color='blue', label='y(t)')
plt.plot(t, y(t)+x(t), color='Yellow', label='Samlet')


xes = np.array([1, 1, 3, 2])
ys = np.array([1, 3, 3, 2])

plt.ylim(-0.1, 3.6)
# plt.xlim(0.9, 3.5)
plt.plot(xes, ys, '*', color='black', label='Points')
plt.grid(True)
plt.legend()

# show the plot
plt.show()