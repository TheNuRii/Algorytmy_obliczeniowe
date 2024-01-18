import numpy as np
import matplotlib.pyplot as plt
import json

def calka_wielomian_pr(wektor_wspolczynkiow, L_prostokatow, dolna_granica, gorna_granica):
    pole = 0
    delta_x = (gorna_granica - dolna_granica)/L_prostokatow
    srodki_przedziałów = np.linspace(dolna_granica + delta_x/2, gorna_granica - delta_x/2, L_prostokatow)
    wysokosci_prostokatow = np.zeros(len(srodki_przedziałów))
    for i in range(len(srodki_przedziałów)):
        wysokosci_prostokatow[i] = wielomian_row(wektor_wspolczynkiow, srodki_przedziałów[i])
        if wysokosci_prostokatow[i] < 0:
            wysokosci_prostokatow[i] = 0

        pole += delta_x * wysokosci_prostokatow[i]

    return pole, wysokosci_prostokatow, srodki_przedziałów


def calka_wielomian_tr(wektor_wspolczynkiow, L_prostokatow, dolna_granica, gorna_granica):
    pole = 0
    wysokosc_trapezu = (gorna_granica - dolna_granica)/L_prostokatow
    granice_przedzialow = np.linspace(dolna_granica, gorna_granica, L_prostokatow + 1)
    dlugosci_bokow = np.zeros(len(granice_przedzialow))
    dlugosci_bokow[0] = wielomian_row(wektor_wspolczynkiow, granice_przedzialow[0])
    if dlugosci_bokow[0] < 0:
        dlugosci_bokow[0] = 0
    for i in range(1, L_prostokatow):
        dlugosci_bokow[i] = wielomian_row(wektor_wspolczynkiow, granice_przedzialow[i])
        if dlugosci_bokow[i] < 0:
            dlugosci_bokow[i] = 0
        pole += (dlugosci_bokow[i - 1] + dlugosci_bokow[i])*wysokosc_trapezu/2
    
    return pole, granice_przedzialow, dlugosci_bokow

def wielomian_row(wielomian, x):
    suma = 0 
    for i in range(len(wielomian)):
        suma += wielomian[i]*x**i
    
    return suma

L_prostokatow = 50
N = 1000
wielomian = np.array(json.loads(input("Podaj wielomian indexuj od wyrazu wolnego: ")))
dolna_granica = float(input("Podaj dolna granice calki: "))
gorna_granica = float(input("Podaj gorna granice calki: "))
x_wiel = np.linspace(dolna_granica, gorna_granica, N)
y_wiel = np.zeros(N)
for i in range(N):
    y_wiel[i] = wielomian_row(wielomian, x_wiel[i])

pole_1, granice_przedzialow, dlugosci_bokow = calka_wielomian_tr(wielomian, L_prostokatow, dolna_granica, gorna_granica)
pole_2, wysokosci_prostokatow, srodki_przedziałów = calka_wielomian_pr(wielomian, L_prostokatow, dolna_granica, gorna_granica)

fig, (ax1, ax2) = plt.subplots(2, 1)
plt.suptitle("Wykresy wielomianów")
ax1.plot(x_wiel, y_wiel, 'r', label="wykres wielomianu")
ax1.bar(granice_przedzialow, dlugosci_bokow, label="Metoda Trapez")
ax1.legend()
ax1.grid()
ax2.plot(x_wiel, y_wiel, 'r', label="wykres wielomianu")
ax2.bar(srodki_przedziałów, wysokosci_prostokatow, label="Metoda - Prostokat")
ax2.legend()
ax2.grid()
plt.show()

print(f"Pole pod krzywą wielomianu (trapez) wynosi: {pole_1}")
print(f"Pole pod krzywą wielomianu (prostoka) wynosi: {pole_2}")