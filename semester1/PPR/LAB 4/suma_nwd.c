#include <stdio.h>

int gcd(int a,int b)
{
    while( a != b )
        if( a < b )
            b -= a;
        else a -= b;
    return a;
}

int x,a,b;
int  s=0;
int main()
{
    scanf("%d",&x);
    a = x;
    scanf(" %d ",&x);
    b = x;
    do
    {
        scanf(" %d",&x);
        if(x==1 &&a && b)
        {
            s+=gcd(a,b);

        }
        else
        {
            b = a;
            a = x;

        }


    }while(x!=0);

    printf("%d",s);



    return 0;
}