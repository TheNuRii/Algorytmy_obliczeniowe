import numpy as np
import matplotlib.pyplot as plt

def calka_kola(R, L):
    delta_x = (2 * R)/L
    rozmiar_przedzialu = np.linspace((delta_x / 2) - R, R - delta_x / 2, L)
    pole = 0
    wysokosci_prosto = np.zeros(L)
    for i in range(L):
        wysokosci_prosto[i] = np.sqrt(R**2 - rozmiar_przedzialu[i]**2)
        pole += wysokosci_prosto[i] * rozmiar_przedzialu[i]
    
    return pole * 2, rozmiar_przedzialu, wysokosci_prosto

L = 10
R = 4
x_kolo = np.linspace(-R, R, 1000)
y_kolo = np.zeros(len(x_kolo))
for i in range(len(x_kolo)):
    y_kolo[i] = np.sqrt(R**2 - x_kolo[i]**2)

pole, srodki_prost, wysokosci_prosto = calka_kola(R, L)

plt.figure()
plt.bar(srodki_prost, wysokosci_prosto)
plt.plot(x_kolo, y_kolo, 'r')
plt.show()

print(f"Pole kola z calki: {pole}")
print(f"Pole kola z biblioteki {np.pi*R**2}")