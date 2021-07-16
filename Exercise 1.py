#Zmienne

a = 100
b = 25.3231
c = 233
d = 10
e = 3
f = 4
imie = "Tomasz "
nazwisko = " Bochniak"
pi = 3.14
Wyniki = "Wyniki operacji matematycznych :  110, 12, 7, 64, 25.32, 258, 28.3231, 25.0, 2, -3.14, Tomasz  Bochniak"    # Nowa zmienna wypisująca wszystkie wyniki operacji matematycznych
l = "Lista: "
L2 = "[1, 23, 12, -32, 8]"
L1 = "Lista po dodaniu trzech elementów: "
l3 = "Lista po usunięciu trzeciego elementu: "
L3 = "[1, 23, -32, 8, 3300, -14, 234]"
l4 = "Lista po usunięciu ostatniego elementu: "
l5= "Długość listy"

#Operacje matematyczne

Wynik1 = a + d
Wynik2 = e * f
Wynik3 = d - e
Wynik4 = f ** e
Wynik5 = round(b, 2)
Wynik6 = int(b) + c
Wynik7 = a / f
Wynik8 = c % e
Wynik9 = -pi
Wynik10 = imie + nazwisko
print(Wyniki)                  #Wyprintowanie wszystkich wyników dodanych do jednej zmiennej

#Operacje na liście

print(l)
Lista1 = [1, 23, 12, -32, 8]

print(L2)


Lista1.append(-14)             # Dodawanie 3 elementów do listy
Lista1.insert(5, 3300)         # Dodawanie elementu w odpowiednie miejsce na liście
Lista1.append(234)             # (mozna również użyć komendy extend i dodać wszystkie trzy argumenty automatycznie na koniec listy.)


print(L1)
print(Lista1)

print(l3)
Lista1.pop(2)                  # Usuwanie trzeciego elemntu z listy
print(L3)
print(l4)

Lista1.pop()                   # Usuwanie ostatniego elementu z listy

print(Lista1)                  # Końcowy efekt :)

print(l5)

print(len(Lista1), "elementów")            # Pokazanie wielkości listy(liczba elementów!! nie indeksów)

