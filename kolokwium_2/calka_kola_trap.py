import numpy as np
import matplotlib.pyplot as plt

def calka_kola(R, L):
    delta_x = (2 * R)/L
    rozmiar_przedzialu = np.linspace(-R, R, L + 1)
    pole = 0
    wysokosci_trap = np.zeros(len(rozmiar_przedzialu))
    wysokosci_trap[0] = np.sqrt(R**2 - rozmiar_przedzialu[0]**2)
    for i in range(1, L):
        wysokosci_trap[i] = np.sqrt(R**2 - rozmiar_przedzialu[i]**2)
        pole += (wysokosci_trap[i - 1] + wysokosci_trap[i])*delta_x/2
    
    return pole * 2, rozmiar_przedzialu, wysokosci_trap

L = 10
R = 4
N = 1000
x_kolo = np.linspace(-R, R, N)
y_kolo = np.zeros(N)
for i in range(N):
    y_kolo[i] = np.sqrt(R**2 - x_kolo[i]**2)

pole, rozmiar_przedzialu, wysokosci_trap = calka_kola(R, L)

plt.figure()
plt.bar(rozmiar_przedzialu, wysokosci_trap)
plt.plot(x_kolo, y_kolo, 'r')
plt. grid()
plt.show()

print(f"Pole kola obliczone calka: {pole}")
print(f"Pole kola obliczone za pomoca biblioteki numpy: {np.pi*R**2}")
