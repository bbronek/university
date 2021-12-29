def gcd(a,b):
    while(b):
        a,b=b,a%b
    return a
a=input().split()
print(gcd(int(a[0]),int(a[1])))