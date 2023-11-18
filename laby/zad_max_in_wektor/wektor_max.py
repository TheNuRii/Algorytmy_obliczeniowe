import numpy as np
import json

wektor = np.array(json.loads(input("Podaj wektor: np. [1, 2]: ")))
wartosc_max = wektor[0]
index = 0

for i in range(len(wektor)):
    if wektor[i] > wartosc_max:
        index = i
        wartosc_max = wektor[i]

print(f"Wartosc maxymalna w tym wektorze: {wartosc_max}, a index tej wartosci: {index}")