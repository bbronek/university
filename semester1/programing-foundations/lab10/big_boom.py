def main():
    x = int(input())
    v = input().split(" ")
    v = [int(x) for x in v]
    for i in v:
        print(f'B{"I"*i}G B{"O"*i}M{"!"*i}')



if __name__ == '__main__':
    main()