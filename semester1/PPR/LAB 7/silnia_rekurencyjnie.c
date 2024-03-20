#include <stdio.h>

int silnia(int n)
{
    if(n<2) return 1;
    return n*silnia(n-1);
}

int n;
int main()
{
    scanf("%d",&n);
    printf("%d",silnia(n));

    return 0;
}