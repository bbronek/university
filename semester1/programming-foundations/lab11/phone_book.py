import sys


def main():
    phone_book = {}
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line == "END":
            break
        entry = line.split(",")
        phone_book[entry[0]] = entry[1]
    for line in sys.stdin:
        line = line.rstrip("\n")
        print(phone_book[line])


if __name__ == "__main__":
    main()
