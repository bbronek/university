from collections import Counter
import sys


def main():
    counts = Counter(line.strip() for line in sys.stdin)
    if counts:
        print(counts.most_common(1)[0][0])


if __name__ == "__main__":
    main()
