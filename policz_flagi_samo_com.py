from lista_flag import stworz_liste_flag


def koncowka_pl( lista_flag):
    
    wynik = 0
    for i,flaga in enumerate( lista_flag):
        if 'com.pl' in flaga or '.herokuapp' in flaga:
            continue
        elif '.com' in flaga:   
            wynik += 1
            print(i, flaga)
            
    return wynik



url = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag( url)
wynik = koncowka_pl( lista_flag)
print()
print("Na stronie jest:", wynik, "domen z końcówką (.com)")
print()





'''
@Banxter
'''