import numpy as np
import matplotlib.pyplot as plt
import json

def calka_wielomian_tr(wektor_wspolczynkiow, L_prostokatow, dolna_granica, gorna_granica):
    pole = 0
    wysokosc_trapezu = (gorna_granica - dolna_granica)/L_prostokatow
    granice_przedzialow = np.linspace(dolna_granica, gorna_granica, L_prostokatow + 1)
    dlugosci_bokow = np.zeros(len(granice_przedzialow))
    dlugosci_bokow[0] = wielomian_row(wektor_wspolczynkiow, granice_przedzialow[0])
    for i in range(1, L_prostokatow):
        dlugosci_bokow[i] = wielomian_row(wektor_wspolczynkiow, granice_przedzialow[i])
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

pole, granice_przedzialow, dlugosci_bokow = calka_wielomian_tr(wielomian, L_prostokatow, dolna_granica, gorna_granica)

plt.figure()
plt.ylim(-1, 20)
plt.bar(granice_przedzialow, dlugosci_bokow)
plt.plot(x_wiel, y_wiel, 'r')
plt.grid()
plt.show()

print(f"Pole pod krzywą wielomianu wynosi: {pole}")