def main():
    v = input().split(" ")
    x = int(v[0])
    y = int(v[1])
    t = input()
    p=[]
    np=[]
    for i in range(x,(y+1)):
        if(i%2):
            np.append(i)
        else:
            p.append(i)
    if t == 'p':
        for i in p:
            print(i,end=" ")
    else:
        for i in np:
            print(i,end=" ")


if __name__ == '__main__':
    main()