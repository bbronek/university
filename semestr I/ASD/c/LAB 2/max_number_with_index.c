#include <stdio.h>
#include <math.h>

int np(int n)
{
    if(n%2) return 1;
    return 0;
}

int n,x,maxi=0,max_index;
int main()
{
    scanf("%d",&n);
    for(int i =0 ;i<n;++i)
    {
        scanf("%d",&x);
        if(x>maxi)
        {
            maxi=x;
            max_index = i+1;
        }


    }
    printf("%d %d",maxi,max_index);


    return 0;
}
