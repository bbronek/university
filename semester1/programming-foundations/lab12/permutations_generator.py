import sys


from itertools import permutations


def main():
    for letters in sys.stdin:
        letters = letters.rstrip("\n")
        letters = sorted(letters)
        for permutation in permutations(letters):
            print("".join(permutation))


if __name__ == "__main__":
    main()
