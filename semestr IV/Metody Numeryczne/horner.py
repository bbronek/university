def horner(w, n, x):
    wynik = w[0] 

    for i in range(1, n):
        wynik = wynik * x + w[i]
    return wynik


n = int(input("Polynomial degree: "))
w = input("polynomial coefficients: ").strip().split()
w = [float(x) for x in w]

z = float(input("x: "))

print("f(x) = : " , horner(w, n, z))
