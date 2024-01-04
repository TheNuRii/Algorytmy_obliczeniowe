import numpy as np
import math
import matplotlib.pyplot as plt

#obliczyc na kartce an a bardziej roznice k
def cos_rek(x, N, err):
    an = 1
    y=1
    for i in range(1, N):
        an = an*(-x*x/(2*i*(2*i)))
        #(-x * x/((2*i+ 2)*(2*i + 1)))
        if abs(an) < err:
            break
        y += an
    return y, i
    

x = np.linspace(-10, 10, 300)

y_rek = np.zeros(len(x))
y_wbudowane = np.cos(x)
liczba_iteracji = np.zeros(len(x))

N = 8
err = 0.1

for i in range(len(x)):
    y_rek[i], liczba_iteracji[i] = cos_rek(x[i], N, err)

fig, (ax1, ax2) = plt.subplots(2, 1)
plt.suptitle("Porównanie wykresów cos(x)")

ax1.set_ylabel("f(x) = cos(x)")
ax1.set_xlabel("x")
ax1.plot(x, y_wbudowane, label="Wykres wbudowanego cos(x)")
ax1.plot(x, y_rek, 'r',label="Wykres cos(x) - rekurencja Tay")
ax1.set_ylim([-3, 3])
ax1.legend()
ax1.grid()

ax2.plot(x, liczba_iteracji, label="wykres liczby wymaganych iteracji Taylora")
ax2.set_ylabel("liczba iteracji")
ax2.set_xlabel("x")
ax2.legend()
ax2.grid()

plt.show()