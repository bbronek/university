import sys

d = {}
x = None
def main():
    for line in sys.stdin:
        line = line.strip()
        if (line not in d):
            d[line] = 1
        else:
            d[line] +=1
    maxi = max(d,key=d.get)
    print(maxi)

if __name__ == '__main__':
    main()