liczba = int(input("Podaj wartość silni: "))

silnia_podanej_liczby = 1

for i in range(1, liczba + 1):
    silnia_podanej_liczby *= i

print(f"Silnia z {liczba} wynosi: {silnia_podanej_liczby}")