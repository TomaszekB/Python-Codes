from random import randint, sample
from time import time


######## FUNKCJA ALGORYTMU WYSZUKIWANIA LINIOWEGO

def linear(line, x):
    for i in range(len(line)):
        if line[i] == x:
            return i
    return None


######## FUNKCJA ALGORYTMU WYSZUKIWANIA BINARNEGO

def binary(line, z):
    x = 0
    y = len(line) - 1

    while y >= x:

        mid = (x + y) // 2

        if line[mid] == z:
            return mid
        if line[mid] < z:
            x = mid + 1
        else:
            y = mid - 1

    return None


####### STWORZENIE BAZY DANYCH (W TYM PRZYPADKU JEST TO ZAKRES LICZB)

baza_danych = sample(range(1000000), 15000)
baza_danych.sort()

szukane = [randint(0, 1000000) for _ in range(9500)]

###### TIMERY/ ZLICZANIE CZASU OD POCZĄTKU DO KONCA FUNKCJI

start = time()
for x in szukane:
    linear(baza_danych, x)
end = time()
algorytm_liniowy = end - start

start = time()
for x in szukane:
    binary(baza_danych, x)
end = time()
algorytm_binarny = end - start

opis = "Główna różnica między wyszukiwaniem liniowym a wyszukiwaniem binarnym polega na tym,\nże wyszukiwanie binarne zajmuje mniej czasu na wyszukanie elementu z posortowanej listy elementów.\nWynika z tego, że skuteczność metody wyszukiwania binarnego jest większa niż wyszukiwanie liniowe."


####### WYNIK KONCOWY

print("Poniżej zostaną wyświetlone czasy wyszukiwania algorytmu liniowego oraz binarnego w zakresie 9500 wyszukiwań na 15000 liczb\n")
print("Wyszukiwanie liniowe:\t", algorytm_liniowy,"\n")
print("Wyszukiwanie binarne:\t", algorytm_binarny,"\n")
print(opis)

