n= int(input())

va = input().strip().split()
va = [int(i) for i in va]
vb = input().strip().split()
vb = [int(i) for i in vb]
for x in vb:
    print(va[x-1],end=" ")