#include <stdio.h>

int n,x;
int main()
{
    scanf("%d",&n);
    int v[n+1];
    if(!(n%2))
    {
        for(int i =1;i<=n;++i)
        {
            scanf("%d",&x);
            if(!(i%2)) v[i] = x;
        }
        for(int i =n;i>=1;i-=2)
        {
            printf("%d ",v[i]);
        }

    }
    else
    {
        for(int i =1;i<=n;++i)
        {
            scanf("%d",&x);
            if(!(i%2)) v[i] = x;
        }
        for(int i =n-1;i>=1;i-=2)
        {
            printf("%d ",v[i]);
        }
    }




    return 0;
}