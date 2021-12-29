#include<stdio.h>
#include<stdlib.h>

long long kroliki(long long  n, long long v[]){
    if( v[n] != -1) return v[n];
    if (n <= 4) return 1;
    if(n==5) v[n] = kroliki(n-1,v) + 3*kroliki(n-4,v);
    else v[n] = kroliki(n-1,v) + 3*kroliki(n-4,v) -2*kroliki(n-5,v);
    return v[n];
}

int main()
{

    int t;
    long long *v,n;
    scanf("%d",&t);
    v = (long long *)malloc((101)*sizeof(long long));
    for(int i =0 ;i<=100;++i)
    {
        v[i] = -1;
    }

    for(int i =0 ;i<t;++i)
    {
        scanf("%lld",&n);
        printf("%lld",kroliki(n,v));
    }



    return 0;
}