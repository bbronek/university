import sys


def main():
    collection = set()
    for line in sys.stdin:
        value = line.rstrip("\n")
        if value == "END COLLECTION":
            break
        collection.add(value)
    for line in sys.stdin:
        print("YES" if line.rstrip("\n") in collection else "NO")


if __name__ == "__main__":
    main()
