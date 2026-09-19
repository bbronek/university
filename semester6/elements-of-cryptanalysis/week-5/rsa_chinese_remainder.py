from math import gcd, isqrt, lcm
from secrets import randbelow


def is_prime(number):
    return number >= 2 and all(
        number % divisor for divisor in range(2, isqrt(number) + 1)
    )


def generate_keypair(p, q):
    if p == q or not is_prime(p) or not is_prime(q) or min(p, q) < 3:
        raise ValueError("Expected two distinct odd primes")
    modulus = p * q
    totient = lcm(p - 1, q - 1)
    exponent = 65537
    if gcd(exponent, totient) != 1:
        exponent = next(
            value for value in range(3, totient, 2) if gcd(value, totient) == 1
        )
    return (exponent, modulus), (pow(exponent, -1, totient), modulus)


def decrypt_crt(ciphertext, p, q, private_exponent):
    if p == q or min(p, q) < 3 or private_exponent <= 0:
        raise ValueError("Invalid private key")
    if not 0 <= ciphertext < p * q:
        raise ValueError("Ciphertext is outside the modulus")
    first = pow(ciphertext, private_exponent % (p - 1), p)
    second = pow(ciphertext, private_exponent % (q - 1), q)
    correction = (first - second) * pow(q, -1, p) % p
    return second + q * correction


def random_prime(lower, upper):
    candidates = [number for number in range(lower, upper) if is_prime(number)]
    if not candidates:
        raise ValueError("The interval contains no primes")
    return candidates[randbelow(len(candidates))]


if __name__ == "__main__":
    p = random_prime(1000, 2000)
    q = random_prime(2000, 3000)
    public, private = generate_keypair(p, q)
    message = 12345
    ciphertext = pow(message, *public)
    print("Ciphertext:", ciphertext)
    print("Decrypted message:", decrypt_crt(ciphertext, p, q, private[0]))
