import sys, string
from itertools import product

alphabet = string.ascii_lowercase


def password_generator(length):
    for letters in product(alphabet, repeat=length):
        yield letters


def main():

    for length in sys.stdin:
        length = length.rstrip("\n")
        length = int(length)
        passwords = password_generator(length)
        for password in passwords:
            print("".join(password))


if __name__ == "__main__":
    main()
