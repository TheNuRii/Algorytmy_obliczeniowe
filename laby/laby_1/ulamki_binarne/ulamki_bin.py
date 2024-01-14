import numpy as np


def dzies2bin(liczba, N):
    liczba_bin = np.zeros(N)
    for i in range(N - 1):
        if liczba * 2 > 1:
            liczba_bin[i] = 1
            liczba -= 1
        liczba *= 2
    return liczba_bin

def blad_wzgledny(ulamek_bin, liczba):
    przeksztalcenie = 0
    for i in range(ulamek_bin.shape[0]):
        przeksztalcenie += (1/(2 ** (i + 1))) * ulamek_bin[i]
        print(przeksztalcenie)
        
    print(przeksztalcenie)
    return abs(liczba - przeksztalcenie)

liczba = float(input("Podaj liczbe: "))
N = int(input("Podaj dokladnosc ulamka (ile miejsc po przecinku): "))
ulamek_bin = dzies2bin(liczba, N)
blad_wzgledny = blad_wzgledny(ulamek_bin, liczba)
print(f"Ulamek w postaci binarnej wynosi: {ulamek_bin} a jego blad przyblienia binarnego wynosi: {blad_wzgledny * 100} %")