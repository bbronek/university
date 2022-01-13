# Bartosz Bronikowski
# Qaszel Airways 02.01.2022

def connection_existence(v, x, y):
    return v[x][y]

def number_of_connections(v, x, n):
    s = 0
    for i in range(0, n):
        s += v[x][i]
    print(s)

def main():
    n, m =  map(int, input().split())
    v = [[0 for x in range(n)] for y in range(n)]

    for x in range(m):
        c = list(map(int, input().split()))
        if (c[0] == 1):
            x = c[1]
            y = c[2]
            v[x][y] = 1
            v[y][x] = 1
        elif (c[0] == 2):
            x = c[1]
            y = c[2]
            v[x][y] = 0
            v[y][x] = 0
        elif (c[0] == 3):
            x = c[1]
            y = c[2]
            if (connection_existence(v, x, y)):
                print("TAK")
            else:
                print("NIE")
        elif (c[0] == 4):
            x = c[1]
            number_of_connections(v ,x, n)
            
if __name__ == '__main__':
    main()
