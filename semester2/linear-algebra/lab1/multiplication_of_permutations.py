def main():
    count = int(input())
    first = input().strip().split()
    first = [int(value) for value in first]
    second = input().strip().split()
    second = [int(value) for value in second]
    for value in second:
        print(first[value - 1], end=" ")


if __name__ == "__main__":
    main()
