#include <stdio.h>

int k=0,l=0;
void rytual(int x)
{

    while(x!=1)
    {
        if(!(x%2))
        {
            k+=1;
            x/=2;
        }
        else
        {
            l+=1;
            x = 3*x+1;
        }

    }
}

int main() {

    int n;
    do {
        k =0;
        l =0;
        scanf("%d", &n);
        if(n==0) break;
        rytual(n);
        if((k+l)<=15)
        {
            printf("%s %d %d","TAK",k,l);
        }
        else
            printf("NIE");


    }while(1);


    return 0;
}
