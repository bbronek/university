#include <stdio.h>

void wypisz(int n)
{
    printf("B");
    for(int i=0;i<n;++i)
    {
        printf("I");
    }
    printf("G B");
    for(int i=0;i<n;++i)
    {
        printf("O");
    }
    printf("M");
    for(int i=0;i<n;++i)
    {
        printf("!");
    }
}
int main(void)
{
    int n,x;
    scanf("%d",&n);
    for(int i = 0;i<n;++i)
    {
        scanf("%d",&x);
        wypisz(x);
    }



    return 0;
}