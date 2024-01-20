import numpy as np

macierz_A = np.array([[1,2,3],
                    [4, 5, 6],
                    [7, 8, 9]])

wiersz_A = macierz_A.shape[0]
kolumna_A = macierz_A.shape[1] 
macierz_B = np.zeros((wiersz_A, kolumna_A))

for w in range(wiersz_A):
    for k in range(kolumna_A):
        macierz_B[wiersz_A - (w + 1)][k] = macierz_A[w,k]

print(f"Macierz koncowa: {macierz_B}")