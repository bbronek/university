def main():
    count = int(input())
    sizes = input().split(" ")
    sizes = [int(count) for count in sizes]
    for size in sizes:
        print(f'B{"I"*size}G B{"O"*size}M{"!"*size}')


if __name__ == "__main__":
    main()
