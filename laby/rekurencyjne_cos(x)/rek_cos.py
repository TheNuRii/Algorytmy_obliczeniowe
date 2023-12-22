import numpy as np
import matplotlib.pyplot as plt

#obliczyc na kartce an a bardziej roznice k
def cos_rek(x, N, err):
    an = 0
    y=x
    for i in range(1, N):
        an += 1

        y += an
    
    return y
    

x = np.linspace(-10, 10, 300)

y_rek = np.zeros(len(x))
y_wbudowane = np.cos(x)

N = 8
err = 0.1
for i in range(len(x)):
    y_rek[i] = cos_rek(x[i], N, err)

fig, (ax1, ax2) = plt.subplots(2, 1)
plt.suptitle("Porównanie wykresów cos(x)")

#ax1.ylabel("f(x) = cos(x)")
#ax1.xlabel("x")
ax1.plot(x, y_wbudowane, label="Wykres wbudowanego cos(x)")
ax1.set_ylim([-3, 3])
ax1.legend()
ax1.grid()

#ax2.ylabel("f(x) = cos(x)")
#ax2.xlabel("x")
ax2.plot(x, y_rek, label="Wykres cos(x) - rekurencja Tay")
ax2.set_ylim([-3, 3])
ax2.legend()
ax2.grid()

plt.show()