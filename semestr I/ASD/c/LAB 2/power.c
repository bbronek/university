#include <stdio.h>

int potega(int n,int m)
{
    int w = 1;
    for(int i = 0;i<m;++i)
    {
        w*=n;
    }
    return(w);

}

int n,m;
int main()
{
    scanf("%d%d",&n,&m);
    printf("%d",potega(n,m));


    return 0;
}