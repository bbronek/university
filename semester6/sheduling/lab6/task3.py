dane_wejsciowe = input().split()
liczba_zadan = int(dane_wejsciowe[0])
liczba_pracownikow = int(dane_wejsciowe[1])
zadania = []
wyniki = []
suma_wynikow = 0

for i in range(liczba_pracownikow):
    dane_wejsciowe = input().split()
    waga = int(dane_wejsciowe[0])
    punkty = int(dane_wejsciowe[1])
    zadania.append([punkty, waga])
    suma_wynikow += waga

zadania.sort()

for i in range(1, max(zadania)[0] + 1):
    najlepsze_zadania = []

    for zadanie in zadania:
        if zadanie[0] == i:
            najlepsze_zadania.append(zadanie[1])

    najlepsze_zadania.sort(reverse=True)

    for j in range(liczba_zadan):
        if len(najlepsze_zadania) > j:
            wyniki.append(najlepsze_zadania[j])
            continue
        wyniki.append(0)

    najlepsze_zadania = najlepsze_zadania[liczba_zadan:]

    for j in najlepsze_zadania:
        najgorsze_zadanie = min(wyniki)
        if j > najgorsze_zadanie:
            for k in range(len(wyniki)):
                if wyniki[k] == najgorsze_zadanie:
                    wyniki[k] = j
                    break

print(suma_wynikow - sum(wyniki))