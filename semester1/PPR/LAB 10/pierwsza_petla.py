a = input()
x = input().split(' ')
for i in x:
    if int(i) >=0:
        print("1", end=" ")
    else:
        print("0",end=" ")