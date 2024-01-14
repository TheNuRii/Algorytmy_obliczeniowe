import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def cos_szereg(x, N):
    suma_szergu = 0
    for i in range(N):
        suma_szergu += (((-1) ** i)  / factorial(2 * i)) * x ** (2 * i)
    
    return suma_szergu

x = np.linspace(-10, 10, 200)
N = len(x)
y_szereg = np.zeros(N)
y = np.zeros(N)

for i in range(N):
    y_szereg[i] = cos_szereg(x[i], 10)
    y[i] = np.cos(x[i])

plt.figure()
plt.ylim([-2, 2])
plt.plot(x, y, label="cos(x) - za pomocą biblioteki numpy")
plt.plot(x, y_szereg, 'r', label="cos(x)- Taylor")
plt.xlabel('x')
plt.ylabel('f(x) = cos(x)')
plt.grid()
plt.legend()
plt.show()
