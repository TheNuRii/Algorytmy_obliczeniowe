import numpy as np
import json

#macierz =  np.array(json.loads(input("Podaj macierz wejsciowa: ")))

macierz_A = np.array([[3, 1, 0, 6],
                    [5, 5, 3, 2],
                    [1, 1, 0, 1]])

wiersz = macierz_A.shape[0]
kolumny = macierz_A.shape[1]


for k in range(kolumny):
    wartosc_max = macierz_A[0][k]
    wartosc_min = macierz_A[0][k]

    for w in range(wiersz):
        if wartosc_max < macierz_A[w][k]:
            wartosc_max = macierz_A[w][k]
        
        if wartosc_min > macierz_A[w][k]:
            wartosc_min = macierz_A[w][k]

    print(f"Dla kolumny {k} martosc max: {wartosc_max} a wartosc min: {wartosc_min}")