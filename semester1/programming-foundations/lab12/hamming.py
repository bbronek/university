from itertools import zip_longest


def distance(left, right):
    return sum(a != b for a, b in zip_longest(left, right, fillvalue=" "))


def main():
    word = input()
    candidates = [input() for _ in range(int(input()))]
    print(
        min(
            candidates,
            key=lambda candidate: distance(word, candidate),
            default="NO SUGGESTIONS",
        )
    )


if __name__ == "__main__":
    main()
