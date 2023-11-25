import numpy as np
import json

macierz_A = np.array([[3, 1, 0, 6],
                    [5, 5, 3, 2],
                    [1, 1, 0, 1]])

wiersz_A = macierz_A.shape[0]
kolumny_A = macierz_A.shape[1]

macierz_B = np.zeros((wiersz_A, kolumny_A))

for w in range(wiersz_A):
    for k in range(kolumny_A):
        macierz_B[w][kolumny_A - (k + 1)] = macierz_A[w][k]

print(f"wynikiem opracji na macierzey jest macierz: {macierz_B}")