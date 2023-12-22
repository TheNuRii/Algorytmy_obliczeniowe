import numpy as np
import matplotlib.pyplot as plt
import json

def wielomian_hornera(x, wsp_wielomianu):
    wartosc_y = 0
    for i in range(wsp_wielomianu.shape[0]):
        wartosc_y += wsp_wielomianu[i] * x ** i
    
    return wartosc_y

#np.array(json.loads(input("Podaj wspolczynki wielomianu (index == potega x): ")))
wsp_wielomianu_1 = np.array([1,1,1])
wsp_wielomianu_2 = np.array([2, 2, 2, 2, 5, 5])
wsp_wielomianu_3 = np.array([3, 3, 3, 1, 6, 1])

x = np.linspace(-10, 10, 1000)
N = len(x)
wielo_1 = np.zeros(N)
wielo_2 = np.zeros(N)
wielo_3 = np.zeros(N)

for i in range(N):
    wielo_1[i] = wielomian_hornera(x[i], wsp_wielomianu_1)
    wielo_2[i] = wielomian_hornera(x[i], wsp_wielomianu_2)
    wielo_3[i] = wielomian_hornera(x[i], wsp_wielomianu_3)

fig, (ax1, ax2, ax3) = plt.subplots(3,1)
plt.suptitle("Wykresy wielomianów")
ax1.plot(x, wielo_1, label="Wykres pierwsej funkcji")
ax1.legend()
ax1.grid()
ax2.plot(x, wielo_1, label="Wykres pierwsej funkcji")
ax2.plot(x, wielo_2, 'r_', label="Wykres drugiej funkcji")
ax2.legend()
ax2.grid()
ax3.plot(x, wielo_1, label="Wykres pierwsej funkcji")
ax3.plot(x, wielo_2, 'r_', label="Wykres drugiej funkcji")
ax3.plot(x, wielo_3, 'g--', label="Wykres trzeciej funkcji")
ax3.legend()
ax3.grid()
plt.ylim(-1000, 1000)
plt.show()
