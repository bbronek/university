def main():
    count = input()
    values = input().split(" ")
    for value in values:
        if int(value) >= 0:
            print("1", end=" ")
        else:
            print("0", end=" ")


if __name__ == "__main__":
    main()
