import numpy as np
import matplotlib.pyplot as plt

def hist_fun(wektor, L_slupkow):
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
    return wektor_h, np.insert(prawe_kranice, 0, x_min),prawe_kranice-rozmiar_przedzialu/2, rozmiar_przedzialu

liczby = np.arange(1000)

