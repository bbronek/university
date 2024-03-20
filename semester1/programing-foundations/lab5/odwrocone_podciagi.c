#include <stdio.h>
#include <stdlib.h>

int a;
int *array;
int main()
{
    scanf("%d",&a);
    array = malloc(a*sizeof(int));
    for(int i =0 ;i<a;++i)
    {
        scanf("%d",&array[i]);
    }
    int s = a%3;
    for(int i =a-1-s ;i>=0;i-=3)
    {
        printf("%d ",array[i]);
    }





    return 0;
}

