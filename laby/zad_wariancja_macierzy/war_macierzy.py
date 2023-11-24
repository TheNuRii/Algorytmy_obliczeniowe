import numpy as np
import json

#macierz = np.array([[1, 2, 3], [4, 5, 6]])
macierz = np.array(json.loads(input("Podaj macierz: np. [[1, 2], [3, 4]]: ")))
srednia = 0
wiersz = macierz.shape[0]
kolumna = macierz.shape[1]

for w in range(wiersz):
    for k in range(kolumna):
        srednia += macierz[w][k]

srednia /= (wiersz * kolumna)

wariancja = 0

for w in range(wiersz):
    for k in range(kolumna):
        wariancja += (macierz[w][k] - srednia) ** 2

print(f"Wartość wariancji tego wektora wynosi: {wariancja / (wiersz * kolumna)}")

