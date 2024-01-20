"""Napisz program, który oblicza średnie osobno z każdego wiersza macierzy wejściowej."""
import numpy as np
import json

#macierz = np.array(json.loads(input("Podaj macierz wejsciowa np. [[1, 2], [3, 4]]: ")))
macierz_A = np.array([[3, 1, 0, 6],
                    [5, 5, 3, 2],
                    [1, 1, 0, 1]])

wiersz = macierz_A.shape[0]
kolumny = macierz_A.shape[1]

for w in range (wiersz):
    srednia_wiersza = 0
    for k in range(kolumny):
        srednia_wiersza += macierz_A[w][k]
    
    print(f"Srednia wiersza o indeksie {w} wynosi: {srednia_wiersza / kolumny}")