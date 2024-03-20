#include <stdio.h>
#include <math.h>

int np(int n)
{
    if(n%2) return 1;
    return 0;
}

int n,x,y,d;
int main()
{
    scanf("%d",&n);
    for(int i =0; i<n;++i)
    {
        scanf("%d%d",&x,&y);
        for(int j=1;j<=x;++j)
        {
            for(int k=1;k<=y;++k)
            {
                scanf("%d",&d);
                if(np(d)) printf("%d (%d,%d)",d,k,j);
            }
        }


    }


    return 0;
}

