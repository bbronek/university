def czas_pracy(n, czasy_raportow):
    suma_czasow = sum(czasy_raportow)
    pojemnosc_plecaka = suma_czasow // 2

    A = [[0] * (pojemnosc_plecaka + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, pojemnosc_plecaka + 1):
            if czasy_raportow[i - 1] <= j:
                A[i][j] = max(A[i - 1][j], A[i - 1][j - czasy_raportow[i - 1]] + czasy_raportow[i - 1])
            else:
                A[i][j] = A[i - 1][j]

    czas_julia = A[n][pojemnosc_plecaka]
    czas_winston = suma_czasow - czas_julia

    return czas_julia, czas_winston

n = int(input())
czasy_raportow = [int(input()) for _ in range(n)]

czas_julia, czas_winston = czas_pracy(n, czasy_raportow)
print(czas_julia, czas_winston)