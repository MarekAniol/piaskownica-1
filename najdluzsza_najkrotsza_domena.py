from lista_flag import stworz_liste_flag

def najkrotsza_najdluzsza_domena( lista_flag):
    
    najkrotsza_najdluzsza = []
    
    for flaga in lista_flag:
        dlugosc_flagi = len( flaga)
        if '.' not in flaga and dlugosc_flagi == 0:
            continue
        najkrotsza_najdluzsza.append( dlugosc_flagi)
        print(dlugosc_flagi)
    return najkrotsza_najdluzsza


    
url = 'https://zajecia-programowania-xd.pl/flagi'
lista_flag = stworz_liste_flag( url)

najkrotsza_najdluzsza = najkrotsza_najdluzsza_domena( lista_flag)
print("Najkrótsza nazwa domeny:",min(najkrotsza_najdluzsza), "znaków.")
print("Najdłuższa nazwa domeny:",max(najkrotsza_najdluzsza), "znaków.")





# Banxter


















### Czarny ###
# from lista_flag import stworz_liste_flag


# def get_min_max(lista_flag):
#     dlugosci = [len(f) for f in lista_flag]
#     najkrotsza = min(dlugosci)
#     najdluzsza = max(dlugosci)
#     return najkrotsza, najdluzsza


# url = 'https://zajecia-programowania-xd.pl/flagi'

# lista_flag = stworz_liste_flag(url)
# shortest, longest = get_min_max(lista_flag)
# print(shortest)
# print(longest)
