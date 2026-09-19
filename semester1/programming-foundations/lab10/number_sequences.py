def main():
    start, end = map(int, input().split())
    parity = input().strip()
    if parity not in {"e", "o"}:
        raise ValueError("Use e for even or o for odd numbers")
    first = start + (start % 2 != (parity == "o"))
    print(*range(first, end + 1, 2))


if __name__ == "__main__":
    main()
