w = input()
n = int(input())
if(n == 0):
    print("BRAK PODPOWIEDZI")
    exit(0)
x = None
l = 0
v =[]
d ={}
for i in range(n):
    l = 0
    x = input()
    d[i] = x
    if len(x) < len(w):
        for c in range(len(x),len(w)):
            x += " "
    else:
        for c in range(len(w), len(x)):
            w += " "
    for i in range(len(x)):
        if(x[i] != w[i]):
            l +=1
    v.append(l)
print(d[v.index(min(v))])