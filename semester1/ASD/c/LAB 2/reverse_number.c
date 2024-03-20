#include <stdio.h>

int odw(int n)
{
    while(n)
    {
        printf("%d",n%10);
        n/=10;
    }

}

int n;
int main()
{
    scanf("%d",&n);
    odw(n);


    return 0;
}