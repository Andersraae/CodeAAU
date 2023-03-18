import numpy as np
import matplotlib.pyplot as plt

def L1(x):
    return 0.5 * x**2 - 5/2 * x + 3

def L2(x):
    return - x**2 + 4 * x - 3

def L3(x):
    return 0.5 * x**2 - 3/2 * x + 1

x = np.linspace(0,4,100) # x start, y start, amount of points

plt.plot(x, L1(x), color='red', label='L1 polynomial')
plt.plot(x, L2(x), color='blue', label='L2 polynomial')
plt.plot(x, L3(x), color='green', label='L3 polynomial')

xes = np.array([1, 2, 3])
ys = np.array([0, 0, 0])

plt.plot(xes, ys, '*', color='black', label='Roots')

print('i: L1(t1) = ' + str(L1(1)) + ' j: L1(t2) = ' + str(L1(2)) + ' L1(t3) = ' + str(L1(3)))
print('i: L2(t2) = ' + str(L2(2)) + ' j: L2(t1) = ' + str(L2(1)) + ' L2(t3) = ' + str(L2(3)))
print('i: L3(t3) = ' + str(L3(3)) + ' j: L3(t1) = ' + str(L3(1)) + ' L3(t2) = ' + str(L3(2)))

plt.grid(True)
plt.legend()

# show the plot
plt.show()