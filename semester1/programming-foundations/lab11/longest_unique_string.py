from collections import Counter
import sys


def main():
    counts = Counter(line.rstrip("\n") for line in sys.stdin)
    unique = [value for value, count in counts.items() if count == 1]
    print(max(reversed(unique), key=len, default=""))


if __name__ == "__main__":
    main()
