import numpy as np
import matplotlib.pyplot as plt

def exp_rek(x, N, err):
    an = x
    y = x
    for i in range(1,N):
        an *= x / (i + 1)
        if abs(an) < err:
            break
        y += an
    return y, i

x = np.linspace(-10, 10, 300)
N =10
err = 0.01

y_rek = np.zeros(len(x))
y_wbudowane = np.exp(x)
liczba_iteracji = np.zeros(len(x))
for i in range(len(x)):
    y_rek[i], liczba_iteracji[i] = exp_rek(x[i], N, err)

fig, (ax1, ax2) = plt.subplots(2, 1)
plt.suptitle("Wyresy funkcji exponecjalnych")

ax1.plot(x, y_wbudowane, label="Wykres wbudowanej funkcji exp(x)")
ax1.plot(x, y_rek, label="Wykres exp(x) - rekurencyjnie Tay", color='r')
ax1.set_xlabel("x")
ax1.set_ylabel("f(x) = exp(x)")
ax1.legend()
ax1.grid()

ax2.plot(x, liczba_iteracji, label="Wykres liczby wymaganych iteracji Taylora")
ax2.set_xlabel('x')
ax2.set_ylabel("liczba iteracji taylora")
ax2.legend()
ax2.grid()

plt.show()