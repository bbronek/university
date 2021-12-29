#include <stdio.h>

int n,v[100],max1,max2;
int main(int argc,char *argv[])
{

    scanf("%d",&n);
    for(int i=0;i<n;++i)
    {
        scanf("%d",&v[i]);
    }
    max1 = v[0];
    max2 = v[0];
    for(int i=0;i<n;++i)
    {
        if(v[i]>max1)
        {
            max2 = max1;
            max1 = v[i];

        }

        else if(v[i]>max2) max2 = v[i];
    }

    printf("%d %d",max1,max2);

    return 0;
}
