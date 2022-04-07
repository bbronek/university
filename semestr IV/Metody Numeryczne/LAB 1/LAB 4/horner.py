def horner(w, n, x):
    wynik = w[0] 

    for i in range(1, n):
        wynik = wynik * x + w[i]
    return wynik


n = int(input("Podaj stopien wielomianu: "))
w = input("Podaj wspolczynniki: ").strip().split()
w = [float(x) for x in w]

z = float(input("Podaj wartość 'z': "))

print("Wartosc wielomianu interpolacyjnego w postaci Newtona w punkcie z wynosi: " , horner(w, n, z))
