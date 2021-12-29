#include <stdio.h>
#include <math.h>

int search(int t[],int n,int x)
{
    for(int i=0;i<n;++i)
    {
        if(t[i] == x) return i+1;
    }
    return 0;
}

int d,n,x;
int main()
{
    scanf("%d",&d);
    for(int i =0 ;i<d;++i)
    {
        scanf("%d",&n);
        int tab[n];
        for(int j=0;j<n;++j)
        {
            scanf("%d",&tab[j]);
        }
        scanf("%d",&x);
        if(search(tab,n,x)) printf("%d",search(tab,n,x));
        else printf("BRAK");

    }



    return 0;
}
