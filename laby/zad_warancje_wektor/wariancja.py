import numpy as np
from math import sqrt
import json

wektor = np.array(json.loads(input("Podaj wektor np. [1, 2]: ")))

n = len(wektor)

srednia_art = sum(wektor) / n

wariancja = 0

for element in wektor:
    wariancja += (element - srednia_art) ** 2

wariancja = sqrt(wariancja / n)

print(f"Wariancja tego wektora wynosi: {wariancja}")