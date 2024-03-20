import sys


def main():
    d = {}
    while(1):
        line = input()
        if line == "KONIEC":
            break
        line = line.split(" -> ")
        x,y = line[0],line[1]
        if x not in d:
            d[x] = []
        if y not in d:
            d[y] = []
        d[x].append(y)
    for line in sys.stdin:
        line = line.rstrip('\n')
        line = line.split(" ? ")
        x, y = line[0], line[1]
        if y in d[x] :
            print("TAK")
        else:
            print("NIE")



if __name__ == '__main__':
    main()