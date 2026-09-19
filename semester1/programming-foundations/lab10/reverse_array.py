def main():
    count = int(input())
    values = input().split(" ")
    values.reverse()
    for value in values:
        print(int(value), end=" ")


if __name__ == "__main__":
    main()
