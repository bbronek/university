def extended_gcd(number, modulus):
    if number == 0:
        return modulus, 0, 1
    gcd, x1, y1 = extended_gcd(modulus % number, number)
    x = y1 - (modulus // number) * x1
    y = x1
    return gcd, x, y


if __name__ == "__main__":
    values = input().strip().split()
    number, modulus = int(values[0]), int(values[1])
    g, x, y = extended_gcd(number, modulus)
    if g != 1:
        print("The number has no modular inverse")
    else:
        print(x % modulus)
