#include <stdio.h>

int wyszukaj(int v[],int n,int x)
{
    int l=0,p =n-1,sr;
    while (l<=p)
    {
        sr = (l+p)/2;
        if(v[sr] ==x) return sr+1;
        if(v[sr]>x) p = sr-1;
        else l = sr + 1;
    }
    return 0;
}

int v[100000],n,m,x;
int main()
{
    scanf("%d",&n);
    for(int i=0;i<n;++i)
    {
        scanf("%d",&v[i]);
    }
    scanf("%d",&m);
    for(int i =0;i<m;++i)
    {
        scanf("%d",&x);
        int w = wyszukaj(v,n,x);
        if(w) printf("%d",w);
        else printf("NIEOBECNY");

    }




    return 0;
}
