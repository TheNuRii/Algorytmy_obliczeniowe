import numpy as np
import matplotlib.pyplot as plt
import math
def roz_normalny(n, srednia, wariancja):
    x = srednia + np.sqrt(wariancja)*np.random.random(n)
    return x

def mediana(wektor):
    wektor = sorted(wektor)
    srdodek = math.floor(len(wektor) / 2)
    if len(wektor) % 2 == 0:
        return (wektor[srdodek + 1] + wektor[srdodek])/2
    else:
        return wektor[srdodek + 1]
    

def hist_fun(wektor, L_slupkow):
    x_min=min(wektor)
    x_max=max(wektor)
    rozmiar_przedzialu=(x_max - x_min)/L_slupkow
    wektor_h=np.zeros(L_slupkow)
    prawe_krance=x_min+np.arange(1, L_slupkow+1)*rozmiar_przedzialu
    for i_probka in range(len(wektor)):
        for i_slupek in range(L_slupkow):
            if wektor[i_probka]<=prawe_krance[i_slupek]:
                wektor_h[i_slupek]+=1
                break
    return wektor_h, np.insert(prawe_krance, 0, x_min), prawe_krance - rozmiar_przedzialu/2, rozmiar_przedzialu

srednia = 12
wariancja=10
N=10000
probki=roz_normalny(N, srednia, wariancja)
L_slupkow=20
licznosc, krance, srodki, delta=hist_fun(probki, L_slupkow)
print(mediana(probki))

plt.figure()
plt.bar(srodki, licznosc)
plt.show()