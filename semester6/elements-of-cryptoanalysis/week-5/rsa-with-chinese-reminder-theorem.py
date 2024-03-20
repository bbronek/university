from sympy import randprime, invert
from random import randint
from math import gcd


def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def generate_keypair(p, q):
    n = p * q
    phi = lcm(p - 1, q - 1)
    e = randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = randint(2, phi - 1)
    d = invert(e, phi)
    return ((e, n), (d, n))


def decrypt_crt(ciphertext, p, q, d):
    d = int(d)
    dp = d % (p - 1)
    dq = d % (q - 1)
    q_inv = invert(q, p)

    m1 = pow(ciphertext, dp, p)
    m2 = pow(ciphertext, dq, q)

    message = (m1 + p * ((q_inv * (m2 - m1)) % p)) % n
    return message


p = randprime(1000, 2000)
q = randprime(2000, 3000)
public, private = generate_keypair(p, q)
d = private[0]
n = private[1]

ciphertext = 987654321
decrypted_message = decrypt_crt(ciphertext, p, q, d)
print(decrypted_message)
