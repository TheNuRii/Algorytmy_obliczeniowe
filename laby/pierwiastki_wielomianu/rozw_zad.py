import numpy as np
import json

def  wylicz_pierwistek(wyraz_wolny, wielomian):
    print(f"pierwiastki podanego wielomianu wynosza: ")
    czy_nie_posiada_pierwiastkow = True
    for i in range(1, abs(wyraz_wolny) + 1):
        if wyraz_wolny % i == 0:
            czy_pierwiastek = 0
            for j in range(1, wielomian.shape[0]):
                czy_pierwiastek += i ** j * wielomian[j]
            if (czy_pierwiastek + wyraz_wolny) == 0:
                print(f"{i}, ")
                czy_nie_posiada_pierwiastkow = False
            czy_pierwiastek = 0
            for j in range(1, wielomian.shape[0]):
                czy_pierwiastek += (-i)**j * wielomian[j]
            
            if (czy_pierwiastek + wyraz_wolny) == 0:
                print(f"{-i}, ")
                czy_nie_posiada_pierwiastkow = False
    if czy_nie_posiada_pierwiastkow:
        print( "Wielomian nie ma rozwiazan")

wielomian = np.array(json.loads(input("Podaj wspolczynki wielomianu w postaci wektora (index == stopien potegi przy x): ")))
ilosc_wspolczynkiow = wielomian.shape[0]

wyraz_wolny = wielomian[0]
wylicz_pierwistek(wyraz_wolny, wielomian)
