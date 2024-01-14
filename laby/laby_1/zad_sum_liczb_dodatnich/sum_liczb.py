suma_podanych_liczb = 0

while suma_podanych_liczb < 100:
    liczba = int(input("podaj liczbę dodatnią, którą chcesz dodać do sumy: "))

    if liczba < 0:
        print("Podano wartość ujemną")
        break

    suma_podanych_liczb += liczba
    print(suma_podanych_liczb)
