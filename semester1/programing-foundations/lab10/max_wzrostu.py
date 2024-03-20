import sys
def main():
    next(sys.stdin)
    v = [int(x) for x in next(sys.stdin).split()]
    print(max(v))

if __name__ == '__main__':
    main()