from lista_flag import stworz_liste_flag

licznik_a = 'a'

def policz_litery_a( lista_flag):
    
    wynik = 0
    for flaga in lista_flag:
        ile_a = flaga.count( licznik_a) 
        wynik += ile_a
    return wynik


url = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag( url)

wynik = policz_litery_a(lista_flag[:-1])
print("Wszystkie flagi zawierają",wynik,"liter(y)",licznik_a)





'''
@Banxter
'''