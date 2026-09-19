import random


def main():
    maximum = int(input())
    count = int(input())
    for number in random.sample(range(1, maximum + 1), count):
        print(number)


if __name__ == "__main__":
    main()
