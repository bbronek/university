def sieve(x,y):
    prime = [True for i in range(y+1)]
    p = 2
    while(p*p<=y):
        if(prime[p] == True):
            for i in range(p*2,y+1,p):
                prime[i] = False
        p += 1
    prime[0], prime[1] = False, False

    for i in range(x,y+1):
        if(prime[i]):
            print(i,end=' ')
if __name__ == '__main__':
    v = input().strip().split()
    sieve(int(v[0]),int(v[1]))