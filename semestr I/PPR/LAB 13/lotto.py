import random


def main():
    n = int(input())
    k = int(input())
    v =[]
    for i in range(k):
        x = random.randint(1,n)
        while x in v:
            x = random.randint(1,n)
        v.append(x)
    for i in v:
        print(i)

if __name__ == '__main__':
    main()