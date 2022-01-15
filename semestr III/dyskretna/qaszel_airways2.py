# Bartosz Bronikowski
# Qaszel Airways 2 13.01.2022

def main():
    n, m =  map(int, input().split())
    keys = [i for i in range(n)]
    v = {key: [] for key in keys}

    for x in range(m):
        c = list(map(int, input().split()))
        if (c[0] == 1):
            x = c[1]
            y = c[2]
            v[x].append(y)
            v[y].append(x)
        elif (c[0] == 4):
            x = c[1]
            print(len(v[x]))
        elif (c[0] == 5):
            x = c[1]
            for city in sorted(v[x]):
              print(city, end=" ")
            print('')
            
if __name__ == '__main__':
    main()
