import sys


def main():
    next(sys.stdin)
    heights = [int(height) for height in next(sys.stdin).split()]
    print(max(heights))


if __name__ == "__main__":
    main()
