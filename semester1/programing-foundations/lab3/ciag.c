#include <stdio.h>

unsigned long v[65536];
_Bool check(int x)
{
    int l = 0 , p =65536;
    int sr;
    while(l<=p)
    {
        sr = (l + p)/2;
        if(v[sr] == x)
            return 1;
        if(v[sr] > x)
            p = sr-1;
        else 
         l = sr +1;

    }
    return 0;
}

int n,d;


int main() 
{


long i = 1 , j = 0;
for( int u = 1 ;u<=65536;++u)
{
    v[u] = i;
    j+=1;
    i+=j;
}

scanf("%d",&n);

for(int i =0 ;i<n;++i)
{
    scanf("%d",&d);
    printf("%d",check(d));
}
 
  
}