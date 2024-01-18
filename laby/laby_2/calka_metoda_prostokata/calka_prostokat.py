import numpy as np
import matplotlib.pyplot as plt
import json

def calka_wielomian(wektor_wspolczynkiow, L_prostokatow, dolna_granica, gorna_granica):
    pole = 0
    delta_x = (gorna_granica - dolna_granica)/L_prostokatow
    srodki_przedziałów = np.linspace(dolna_granica + delta_x/2, gorna_granica - delta_x/2, L_prostokatow)
    wysokosci_prostokatow = np.zeros(len(srodki_przedziałów))
    for i in range(len(srodki_przedziałów)):
        wysokosci_prostokatow[i] = roz_wielomianu(wektor_wspolczynkiow, srodki_przedziałów[i])
        if wysokosci_prostokatow[i] < 0:
            wysokosci_prostokatow[i] = 0

        pole += delta_x * wysokosci_prostokatow[i]

    return pole, wysokosci_prostokatow, srodki_przedziałów

def roz_wielomianu(wielomian, x):
    suma = 0
    for i in range(len(wielomian)):
        suma += wielomian[i] * x**i
    
    return suma


wielomian =  np.array(json.loads(input("Podaj wielomian indexuj od wyrazu wolnego: ")))
dolna_granica = float(json.loads(input("Podaj przedzial calkowania od a: ")))
gorna_granica = float(json.loads(input("Podaj przedzial calkowania do b: ")))
x_wiel = np.linspace(-10, 10, 1000)
y_wiel = np.zeros(len(x_wiel))
L_prostokatow = 20

for i in range(len(x_wiel)):
    y_wiel[i] = roz_wielomianu(wielomian, x_wiel[i])

pole, wysokosci_prostokatow, srodki_przedziałów = calka_wielomian(wielomian, L_prostokatow, dolna_granica, gorna_granica)

plt.figure()
plt.ylabel("f(x)")
plt.xlabel("x")
plt.ylim(-1, 20)
plt.bar(srodki_przedziałów, wysokosci_prostokatow)
plt.plot(x_wiel, y_wiel, 'r')
plt.grid()
plt.show()

print(f"Pole pod krzywą wielomianu wynosi: {pole}")