from lista_flag import stworz_liste_flag

def koncowka_pl( lista_flag):
    
    wynik = 0
    for flaga in lista_flag:
        if '.pl' in flaga:
            wynik += 1
            
    return wynik

url = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag( url)
wynik = koncowka_pl( lista_flag)

print("Na stronie jest:", wynik, "domen z końcówką (.pl)")





'''
@Banxter
'''