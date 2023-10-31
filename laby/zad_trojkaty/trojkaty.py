import math

bok_a = float(input("podaj wartość pierwszego boku: "))
bok_b = float(input("podaj wartość drugiego boku: "))
bok_c = float(input("podaj wartość trzeciego boku: "))

zbior_bokow = [bok_a, bok_b, bok_c]
zbior_bokow.sort()


if (bok_a + bok_b > bok_c) and (bok_a + bok_c > bok_b) and (bok_b + bok_c > bok_a):
   
    cos_a = (bok_b**2 + bok_c**2 - bok_a**2) / (2 * bok_b * bok_c)
    cos_b = (bok_a**2 + bok_c**2 - bok_b**2) / (2 * bok_a * bok_c)
    cos_c = (bok_a**2 + bok_b**2 - bok_c**2) / (2 * bok_a * bok_b)

    zbior_katow = [math.degrees(cos_a), math.degrees(cos_b), math.degrees(cos_c)]

    if bok_a == bok_b == bok_c:
        print("Dana figura jest trójkątem równobocznym")

    elif (bok_a == bok_b) or (bok_a == bok_c) or (bok_b == bok_c):
        print("Dana figura jest trójkątem równoramiennym")

    elif zbior_bokow[0]**2 + zbior_bokow[1]**2 == zbior_bokow[2]**2:
        print("Dana figura jest trójkątem prostokątnym")
    
    elif zbior_bokow[0] < 90 and zbior_katow[1] < 90 and zbior_katow[2] < 90:
        print("Dana figura jest trójkątem ostrokątnym")

    elif  90 < max(zbior_katow) < 180:
        print("Dana figura jest trójkątem rozwartokątnym")

    elif bok_a != bok_b != bok_c:
        print("Dana figura jest trójkątem różnoboczny")

    else:
        print("Dana figura jest trójkątem")
else:
    print("z podanych boków nie można zbudować trójkąta")