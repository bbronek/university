def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


if __name__ == "__main__":
    v = input().strip().split()
    a, b = int(v[0]), int(v[1])
    g, x, y = extended_gcd(a, b)
    if g != 1:
        print("The number has no modular inverse")
    else:
        print(x % b)
