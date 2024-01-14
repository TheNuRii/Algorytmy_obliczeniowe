podstawa = float(input("Podaj podstawę liczby potęgowanej: "))
potega = int(input("Podaj potęgę liczby: "))

def potegowanie_log(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        return potegowanie_log(a, n/2) * potegowanie_log(a, n/2)
    elif n % 2 != 2:
        return(potegowanie_log(a, n - 1)) * a

if podstawa == 0 and potega == 0:
    print("0 do potęgi 0 jest symbolem nieoznaczonym")
elif potega == 0:
    print(1)
else:
    print(f"Potęga z podanych wartości wynosi: {potegowanie_log(podstawa, potega)}")
    
