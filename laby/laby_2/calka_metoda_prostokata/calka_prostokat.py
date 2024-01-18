import numpy as np
import matplotlib.pyplot as plt
import json

def calka_wielomian(wektor_wspolczynkiow, L_prostokatow, dolna_granica, gorna_granica):
    pass

def roz_wielomianu(wielomian, x):
    suma = 0
    for i in range(len(wielomian)):
        suma += wielomian[i] * x**i
    
    return suma

wielomian =  np.array(json.loads(input("Podaj wielomian indexuj od wyrazu wolnego: ")))
a_przedzial = float(json.loads(input("Podaj przedzial calkowania od a: ")))
b_przedzial = float(json.loads(input("Podaj przedzial calkowania do b: ")))
x_wiel = np.linspace(-10, 10, 1000)
y_wiel = np.zeros(len(x_wiel))

for i in range(len(x_wiel)):
    y_wiel[i] = roz_wielomianu(wielomian, x_wiel[i])

plt.figure()
plt.ylim(0, 1000)
plt.ylabel("f(x)")
plt.xlabel("x")
plt.plot(x_wiel, y_wiel, 'r')
plt.grid()
plt.show()


