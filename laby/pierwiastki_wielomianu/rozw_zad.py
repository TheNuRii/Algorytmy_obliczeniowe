import numpy as np
import json

def wylicz_pierwistek(wyraz_wolny, wielomian):
    for i in range(1, wielomian.shape[0]):
        print(i)
        if wyraz_wolny % i == 0:
            czy_pierwiastek = 0
            for j in range(1, wielomian.shape[0]):
                czy_pierwiastek += i ** j * wielomian[j]
            if (czy_pierwiastek + wyraz_wolny) == 0:
                return i
            czy_pierwiastek = 0
            for j in range(1, wielomian.shape[0]):
                czy_pierwiastek += (-i)**j * wielomian[j]
                print(czy_pierwiastek)
            if (czy_pierwiastek + wyraz_wolny) == 0:
                return -i

    return "Wielomian nie ma rozwiazan"

wielomian = np.array(json.loads(input("Podaj wspolczynki wielomianu w postaci wektora (index == stopien potegi przy x): ")))
ilosc_wspolczynkiow = wielomian.shape[0]

wyraz_wolny = wielomian[0]
pierwiastki = np.zeros(ilosc_wspolczynkiow)
pierwiastki[0] = wylicz_pierwistek(wyraz_wolny, wielomian)

print(pierwiastki)
