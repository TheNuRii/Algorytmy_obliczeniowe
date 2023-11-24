import numpy as np
import json

#macierz_A = np.array([[1, 2, 3], [4, 5, 6]])
#macierz_B = np.array([[1, 2, 3], [4, 5, 6]])
macierz_A = np.array(json.loads(input("Podaj macierz A: ")))
macierz_B = np.array(json.loads(input("Podaj macierz B: ")))

wiersz_A = macierz_A.shape[0]
kolumna_A = macierz_A.shape[1]

wiersz_B = macierz_B.shape[0]
kolumna_B = macierz_B.shape[1]



if (wiersz_A == wiersz_B) and (kolumna_A == kolumna_B):
    macierz_C = np.zeros((wiersz_A, kolumna_A))
    for w in range(wiersz_A):
        for k in range(kolumna_A):
            macierz_C[w][k] += macierz_A[w][k] + macierz_B[w][k]

    print(f"Suma tych dwoch macierzy wynosi: {macierz_C}")

else:
    print("Nie mozna dodac tych dwoch macierzy, bo wymiary sie roznia")