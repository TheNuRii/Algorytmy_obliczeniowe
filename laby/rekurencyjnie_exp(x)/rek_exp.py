import numpy as np
import matplotlib.pyplot as plt

def exp_rek(x, N, err):
    an = 0
    y = x
    for i in range(1,N):
        an += 1
        an = y
    
    return y

x = np.linspace(-10, 10, 300)

y_rek = np.zeros(len(x))
y_wbudowane = np.exp(x)

N =10
err = 0.01

for i in range(len(x)):
    y_rek[i] = exp_rek(x[i], N, err)

fig, (ax1, ax2) = plt.subplots(2, 1)
plt.suptitle("Wyresy funkcji exponecjalnych")

ax1.plot(x, y_wbudowane, label="Wykres wbudowanej funkcji exp(x)")
ax1.legend()
ax1.grid()

ax2.plot(x, y_rek, label="Wykres exp(x) - rekurencyjnie Tay")
ax2.legend()
ax2.grid()

plt.show()