#include <stdio.h>

float j,x,y,z;
int main(void)
{
    scanf("%f%f%f%f",&j,&x,&y,&z);
    printf("%.2f",(z-(x*j))/y);

    return 0;
}