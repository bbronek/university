#include <stdio.h>

int n,v[1000];

int main()
{

    scanf("%d",&n);
    scanf("%d",&v[0]);
    int max = v[0],c=1;;

    for(int i=1;i<n-1;++i)
    {
        scanf("%d",&v[i]);

        if(max<v[i])
        {
            max = v[i];
            c = 1;
        }

        if(max == v[i]) c+=1;

    }

    printf("%d",c);



    return 0;
}