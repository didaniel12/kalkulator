# name = input("twoje imię: ")
# print("cześć " + name)
# a = input("liczba 1 ")
# b = input("liczba 2 ")
# print(int(a) + int(b))
# print(type("a")) 
# print("dadad")

def kalkulator():
    a = str(input('Podaj pierwsza liczbe: '))
    b = str(input('Podaj druga liczbe (kurwa): '))
    opcja = str(input("podaj opcje \"/, +, -, *\": "))

    def dzialanie(a,b ,opcja):
        string = a+opcja+b;
        return eval(string); 
    try:
        wynik = float(dzialanie(a, b, opcja));
        # print(wynik)
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