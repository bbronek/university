import random

def is_prime(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def find_prime(bits=16):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

def find_primitive_root(p):
    for g in range(2, p):
        if all(pow(g, power, p) != 1 for power in range(1, p-1)):
            return g
    return None

def generate_keys(p):
    g = find_primitive_root(p)
    x = random.randint(2, p-2)
    h = pow(g, x, p)
    return g, h, x

def encrypt(g, h, p, m):
    y = random.randint(2, p-2)
    c1 = pow(g, y, p)
    s = pow(h, y, p)
    c2 = (m * s) % p
    return c1, c2

def decrypt(c1, c2, p, x):
    s = pow(c1, x, p)
    m = (c2 * pow(s, p-2, p)) % p
    return m

p = find_prime()
g, h, x = generate_keys(p)
m = 123
c1, c2 = encrypt(g, h, p, m)
print('Cipher text:', c1, c2)
m = decrypt(c1, c2, p, x)
print('Decrypted text:', m)
