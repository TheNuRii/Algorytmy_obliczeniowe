import numpy as np

N =  int(input("Podaj wymiary macierzy trojkatnej lewostronnej: "))

macierz = np.zeros((N, N))
licznik = 1

for w in range(N):
    for k in range(N):
        if w + k < 3:
            macierz[w][k] += licznik
            licznik += 1
        
print(f"Macierz trojkatna wynosi: {macierz}")