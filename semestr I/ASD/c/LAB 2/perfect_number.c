#include <stdio.h>

int doskonala(int n)
{
    int s = 1;
    for(int i = 2;i<n;++i)
    {
        if(!(n%i)) s+=i;
    }
    return(s==n);

}

int n;
int main()
{
    scanf("%d",&n);
    if(doskonala(n)) printf("tak");
    else printf("nie");

    return 0;
}

