#include <stdio.h>

long long  fib(long long n)
{
    if(n==0) return 0;
    long long a = 0;
    long long b= 1;
    for(int i=2;i<=n;++i)
    {
        b +=a;
        a = b-a;
    }
    return b;
}

long long n;
int main()
{
    scanf("%llu",&n);
    printf("%llu",fib(n));



    return 0;
}
