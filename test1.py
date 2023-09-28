def dzielenie(a , b):
    return a / b
a = input("wpisz liczbę ")
b = input(" wpisz liczbę: ")
try:
    b = float(b)
    a = float(a)
    wynik = a / b
    a % b
    if a % b == 0:
        print(int(wynik))
    else: print(wynik)
    
except ValueError:
    print("twoja stara")
except ZeroDivisionError:
    print("masz downa?")