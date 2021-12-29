import sys
W1 = [int(x) for x in next(sys.stdin).split()]
M1 = []
for line in range(W1[0]):
    M1.append([float(x) for x in next(sys.stdin).split()])
W2 = [int(x) for x in next(sys.stdin).split()]
if W1[1] == W2[0]:
    M2 = []
    for line in range(W2[0]):
        M2.append([float(x) for x in next(sys.stdin).split()])
    R = [[float(0) for i in range(W2[1])] for j in range(W1[0])]
    for i in range(0, W1[0]):
        for j in range(0, W2[1]):
            for k in range(0, W1[1]):
                R[i][j] += M1[i][k] * M2[k][j]
    for line in R:
        for item in line:
            print("{:.1f} ".format(item), end='')
        print("\n", end="")
else:
    print("ERROR")