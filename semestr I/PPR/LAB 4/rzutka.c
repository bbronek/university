#include <stdio.h>

int x,y,n,r,s;
int main()
{
    scanf("%d%d",&x,&y);
    scanf("%d",&n);
    for(int i = 0;i<n;++i)
    {
        scanf("%d",&r);
        if(r<x) s+=x-r;
        if(r>y) s+=r-y;
        if(r>=x&&r<=y) s=0;

    }
    printf("%d",s);



    return 0;
}