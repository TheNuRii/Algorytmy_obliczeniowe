import numpy as np
import matplotlib.pyplot as plt

def roz_normalny(N, srednia, wariancja):
    x = srednia + np.sqrt(wariancja)*np.random.rand(N)
    return np.round(10+12*x)

def oblicz_srednia(x):
    suma = 0
    for i in range(len(x)):
        suma+= x[i]

def oblicz_waranacje(x, srednia):
    suma = 0
    for i in range(len(x)):
        suma += (x[i] - srednia) ** 2

    return suma / len(x)

def oblicz_dominante(wektor):
    elementy = np.zeros(len(wektor))
    

N = 1000
f_x = roz_normalny(N, 10, 3)
srednia = oblicz_srednia(f_x)
warancja = (f_x, srednia)


plt.figure()
plt.plot(f_x)
plt.show()