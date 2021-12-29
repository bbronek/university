from functools import reduce
def gcf(a,b):
    fa = a
    fb = b
    while b:
        a,b = b,a%b
    return (fa*fb)/a

def transposition(x):
    for i in range(1,len(x)):
        print("(%d,%d)"%(x[0],x[len(x)-i]),end='')

def cykle(p):
    p = {i+1: p[i] for i in range(len(p))}
    cycles = []
    while p:
        e = next(iter(p))
        curr = p[e]
        nextt = p[curr]
        cycle = []
        while True:
            if curr != nextt:
                cycle.append(curr)
            del p[curr]
            curr = nextt
            if nextt in p:
                nextt = p[nextt]
            else:
                break
        rc = []
        if len(cycle) != 0 :
            rc.append(cycle[len(cycle)-1])
            rc.append(cycle[0])
            for i in range(1,len(cycle)-1):
                rc.append(cycle[i])
        cycles.append(rc)
    return cycles
n = int(input())
v = input().strip().split()
v = [int(i) for i in v]


r = cykle(v)
g = []
s = 0
for i,x in enumerate(r):
    if len(x) == 0:
        del r[i]
    else:
        g.append(len(x))
        s += len(x)-1
rz = reduce(gcf,g)  # order of permutation

for i in range(len(r)):
    print('(',end='')
    print('{},'.format(r[i][0]),end='')
    for j in range(1,len(r[i])-1):
        print("{},".format(r[i][j]),end='')
    print("%d)"%(r[i][len(r[i])-1]),end='')
print('\n%d'%rz)

for x in r:
    transposition(x)
if(s%2):
    print('\nnieparzysta')
else:
    print('\nparzysta')
