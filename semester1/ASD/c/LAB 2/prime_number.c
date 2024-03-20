#include <stdio.h>

int pierwsza(int n)
{
    if(n<2)
        return 0;
    for(int i = 2;i<=sqrt(n);++i)
    {
        if(!(n%i)) return 0;
    }
    return 1;
}

int n,x;
int main()
{
    scanf("%d",&n);
    for(int i=0;i<n;++i)
    {
        scanf("%d",&x);
        if(pierwsza(x)) printf("PIERWSZA");
        else printf("ZLOZONA");
    }

    return 0;
}
