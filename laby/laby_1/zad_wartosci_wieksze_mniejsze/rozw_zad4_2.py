import numpy as np
import json


wektor =  np.array(json.loads(input("Podaj wektor w postaci: np. [1, 2]: ")))

wartosc_srednia = sum(wektor) / len(wektor)
wieksze_od = 0
mniejsze_od = 0

for elment in wektor:
    if elment > wartosc_srednia:
        wieksze_od += 1
    elif elment < wartosc_srednia:
        mniejsze_od += 1

print(f"Wartosc srednia wektora wynosi: {wartosc_srednia}, jest {wieksze_od} wartosci wiekszych od tej sredniej i jest {mniejsze_od} wartosci mniejszych od tej sredniej")



