
liczba_uzyskanych_punktow = int(input("Podaj ilość zdobytch przez ciebie punktów: "))
maksymalna_liczba_punktow = int(input("Podaj maksymalną ilość punktów do zdobycia: "))

wynik_procentowy = float(liczba_uzyskanych_punktow / maksymalna_liczba_punktow) * 100

if 0 <= wynik_procentowy < 50:
    print("ocena niedostateczna")
elif 50 <= wynik_procentowy < 70:
    print("ocena dostateczna")
elif 70 <= wynik_procentowy < 90:
    print("ocena dobra")
elif 90 <= wynik_procentowy <= 100:
    print("ocena bardzo dobra")
else:
    print("Nieprawłowo podane wartości wejściowe")