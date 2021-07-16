from random import *

Lista = []

liczbyUzytkownika = 6

while liczbyUzytkownika > 0:
    try:
        cyfra = input("Wprowadź liczbę z podanego zakresu od 1 do 49: ")
        cyfra = int(cyfra)

        if cyfra in range(1, 50):
            if cyfra in Lista:
                print("Podałeś już tę liczbę!Spróbuj podać inną!")
            else:
                Lista.append(cyfra)
                liczbyUzytkownika = liczbyUzytkownika - 1

        elif cyfra > 49 or cyfra < 1:
            print("Podana liczba nie znajduje się w obowiązywanym zakresie!")
    except ValueError:
        print("Podaj liczbę!")

Lista.sort()
print("Twoje liczby to: " + str(liczbyUzytkownika))

zakresLotto = range(1, 50)
Lotto = list(zakresLotto)
shuffle(Lotto)
lotto_wylosowane = (Lotto[:6])
lotto_wylosowane.sort()
print("Maszyna losująca wylosowała następujące liczby: " + str(lotto_wylosowane))

count = 0

for item in Lista:
    if item in lotto_wylosowane:
        count += 1

Mozliwosci = {6: "Trafiłeś szóstkę!", 5: "Trafiłeś piątkę!", 4: "Trafiłeś czwórkę!", 3: "Trafiłeś trójkę!"}
wynik = Mozliwosci.get(count, "Niestety ale tym razem Ci się nie udało. Powodzenia następnym razem!")

print(wynik)
