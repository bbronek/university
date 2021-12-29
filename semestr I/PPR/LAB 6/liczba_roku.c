#include <stdio.h>
#include <stdlib.h>

int ile(int v[],int x,int n)
{
    int l =0;
    for(int i=0;i<n;++i)
    {
        if(!(x%v[i])) l+=1;
    }
    return l;
}

int n,m,*v,x;
int main() {

    scanf("%d",&n);
    v = malloc(n * sizeof(int));

    for(int i=0;i<n;++i)
    {
        scanf("%d",&v[i]);
    }

    scanf("%d",&m);

    for(int i=0;i<m;++i)
    {
        scanf("%d",&x);
        printf("%d",ile(v,x,n));

    }



    return 0;
}