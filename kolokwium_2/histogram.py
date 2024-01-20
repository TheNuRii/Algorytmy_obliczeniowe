import numpy as np
import matplotlib.pyplot as plt



""" def hist_fun(wektor, L_slupkow):
    x_min=min(wektor)
    x_max=min(wektor)
    rozmiar_przedzialu=(x_max - x_min)/L_slupkow
    wektor_h = np.zeros(L_slupkow)
    prawe_kranice = x_min + np.linspace(x_min + rozmiar_przedzialu/2, x_max + rozmiar_przedzialu/2, L_slupkow + 1)
    for i_probka in range(len(wektor)):
        for i_slupek in range(L_slupkow):
            if wektor[i_probka] <= prawe_kranice[i_slupek]:
                wektor_h[i_slupek] += 1
                break
    wektor_h=wektor_h/(rozmiar_przedzialu*len(wektor))
    return wektor_h, np.insert(prawe_kranice, 0, x_min),prawe_kranice-rozmiar_przedzialu/2, rozmiar_przedzialu


def dystrybuanta(wektor, srodki):
    cdf = np.zeros(len(srodki))
    delta_x = srodki[1] - srodki[0]
    cdf[0] = wektor[0]*delta_x
    for i in range(1, len(wektor)):
        cdf[i] = cdf[i -1] + wektor[i]*delta_x
    
    return cdf """


L_slupkow = 20
N = 1000
liczby = np.arange(1000)
for i in range(N):
    suma_liczb = sum(np.random.randint(1, 10)  for _ in range(10))
    liczby[i] = suma_liczb
print(liczby)
srednia = sum(liczby)/len(liczby)
warjancja = sum((x - srednia)**2 for x in liczby) / len(liczby)

plt.figure()
plt.hist(liczby, bins=range(10, 101), edgecolor='black')
plt.xlabel("X")
plt.ylabel("P(X = xi)")
plt.title("Hisogram")
plt.show()
print(f"Srednia: {srednia}")
print(f"Warjancja: {warjancja}")


