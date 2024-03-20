import math
from statistics import mean

def average(x):
    return mean(x)

def pearson(x, y):
    n = len(x)
    ax = average(x)
    ay = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for i in range(n):
        xdiff = x[i] - ax
        ydiff = y[i] - ay
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff
    downx = math.sqrt(xdiff2)
    downy = math.sqrt(ydiff2)
    down = downx*downy
    return diffprod/down


def main():
    vx = []
    vy = []
    x = int(input())
    for line in range(x):
        line = input()
        line = line.strip().split()
        vx.append((line[0]))
        vy.append((line[1]))
    vx = [int(x) for x in vx]
    vy = [int(x) for x in vy]
    print(f'{pearson(vx,vy):.2f}')

if __name__ == '__main__':
    main()