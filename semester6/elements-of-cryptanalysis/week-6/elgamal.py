from math import isqrt
from secrets import randbelow, randbits


def is_prime(number):
    return number >= 2 and all(
        number % divisor for divisor in range(2, isqrt(number) + 1)
    )


def find_prime(bits=16):
    if bits < 3:
        raise ValueError("Use at least three bits")
    while True:
        candidate = randbits(bits) | (1 << (bits - 1)) | 1
        if is_prime(candidate):
            return candidate


def find_primitive_root(prime):
    if not is_prime(prime) or prime < 5:
        raise ValueError("Expected a prime of at least five")
    remainder = prime - 1
    factors = set()
    divisor = 2
    while divisor * divisor <= remainder:
        while remainder % divisor == 0:
            factors.add(divisor)
            remainder //= divisor
        divisor += 1
    if remainder > 1:
        factors.add(remainder)
    return next(
        generator
        for generator in range(2, prime)
        if all(pow(generator, (prime - 1) // factor, prime) != 1 for factor in factors)
    )


def generate_keys(prime):
    generator = find_primitive_root(prime)
    private_key = randbelow(prime - 3) + 2
    return generator, pow(generator, private_key, prime), private_key


def encrypt(generator, public_key, prime, message):
    if not 0 <= message < prime:
        raise ValueError("Message must be between zero and prime - 1")
    ephemeral_key = randbelow(prime - 3) + 2
    return (
        pow(generator, ephemeral_key, prime),
        message * pow(public_key, ephemeral_key, prime) % prime,
    )


def decrypt(first, second, prime, private_key):
    if not 0 < first < prime or not 0 <= second < prime:
        raise ValueError("Ciphertext is outside the field")
    shared_secret = pow(first, private_key, prime)
    return second * pow(shared_secret, -1, prime) % prime


if __name__ == "__main__":
    prime = find_prime()
    generator, public_key, private_key = generate_keys(prime)
    first, second = encrypt(generator, public_key, prime, 123)
    print("Ciphertext:", first, second)
    print("Decrypted message:", decrypt(first, second, prime, private_key))
