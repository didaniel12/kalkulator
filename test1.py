# name = input("twoje imię: ")
# print("cześć " + name)
# a = input("liczba 1 ")
# b = input("liczba 2 ")
# print(int(a) + int(b))
# print(type("a")) 
# print("dadad")

def kalkulator():
    a = input('Podaj pierwsza liczbe: ')
    b = input('Podaj druga liczbe (kurwa): ')
    opcja = input("podaj opcje \":, +, -, *\": ")

    def dzielenie(a,b):
        return a / b
    def dodawanie(a, b):
        return a+b
    def odejmowanie(a, b):
        return a-b
    def mnozenie(a, b):
        return a*b
    try:
        a = float(a)
        b = float(b)
        wynik = 0;
        if (opcja == ':'):
            wynik = dzielenie(a , b)
        elif (opcja == '+'):
            wynik = dodawanie(a, b)
        elif (opcja == "-"):
            wynik = odejmowanie(a, b)
        elif (opcja == '*'):
            wynik = mnozenie(a ,b)
        
        # >>> (1.0).is_intiger()
        # <<< True
        # >>> (1.55).is_intiger()
        # <<< False

        if wynik.is_integer(): 
            wynik = int(wynik)
        print(wynik)
        # jak juz masz wynik to znowu wywolaj kalkulator
        kalkulator()

    except:
        print('Twoje dane sa zjebane!')

kalkulator() # wywolaj funckje kalkulator poraz pierwszy