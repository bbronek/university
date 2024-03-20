def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

if __name__ == '__main__':
    v = input().strip().split()
    a,b = int(v[0]), int(v[1])
    g, x, y = gcdExtended(a,b)
    if(g!=1): print("liczba nie jest odwracalna")
    else:
        if(x>0):print(x)
        else: print(b+x)

