def main():
    int(input())

    v = input()

    return sum(list(map(int, v.split(' '))))

if __name__ == '__main__':
    print(main())