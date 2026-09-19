from collections import Counter


import sys


def main():
    for line in sys.stdin:
        line = line.rstrip("\n").split()
        first, second = line[0], line[1]
        if Counter(first) == Counter(second):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
