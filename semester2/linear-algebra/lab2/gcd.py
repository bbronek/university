def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    a = input().split()
    print(gcd(int(a[0]), int(a[1])))


if __name__ == "__main__":
    main()
