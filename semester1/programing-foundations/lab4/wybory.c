#include <stdio.h>

int max(int k[],int n)
{
    int m=1,w=1;
    for(int i =1;i<=n;++i)
    {
        if(k[i]>m)
        {
            m = k[i];
            w=i;
        }

    }
    return w;
}

int n,m,x;
int main()
{
    scanf("%d%d",&n,&m);
    int k[n+1];
    for(int i=1;i<=n;++i)
    {
        k[i]=0;
    }
    for(int i=0;i<m;++i)
    {
        scanf("%d",&x);
        k[x]++;
    }
    for(int j=1;j<=n;++j)
    {
        printf("%d:%d ",j,k[j]);
    }
    printf("%d",max(k,n));

    return 0;
}