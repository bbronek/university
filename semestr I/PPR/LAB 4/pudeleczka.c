#include <stdio.h>

int sum(int v[],int a,int b)
{
    int s = 0;
    for(int i = a-1;i<=b-1;++i)
    {
        s+=v[i];
    }
    return s;
}

int x,y,d,a,b;
int main()
{
    scanf("%d",&x);
    int v[x];
    for(int i=0;i<x;++i)
    {
        scanf("%d",&v[i]);
    }
    scanf("%d",&y);
    for(int i=0;i<y;++i)
    {
        scanf("%d%d",&a,&b);
        printf("%d",sum(v,a,b));

    }


    return 0;
}