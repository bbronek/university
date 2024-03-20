from functools import reduce
matrix = []
def third_step(f,v,j):
    for x in range(len(v)):
        for y in range(len(v[0])):
            v[x][y] -= f[y] * v[x][j]


def rref(matrix):
    R = matrix
    i,j = 0,0

    while True:
        if (i == len(R) - 1) : break
        while(R[i][j] != 0):
            R[0],R[i] = R[i],R[0]
            R[0] = list(map(lambda x:x/R[i][j],R[i]))
            third_step(R[0],R[1:],j)
            if (i == len(R) - 1): break
            if((j == len(R[0]) - 1)):
                i += 1
                j = 0
            else:
                j += 1
        if(R[i][j] != 0):
            j+=1
    return R


if __name__ == '__main__':
    line = input()
    line = line.strip().split()
    line = [int(i) for i in line]
    m,n = line[0],line[1]
    for i in range(m):
        line2 = input()
        line2 = line2.strip().split()
        line2 = [int(i) for i in line2]
        matrix.append(line2)

    print(rref(matrix))



