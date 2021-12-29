#include <stdio.h>

void avg(double s,int n)
{
    printf("%.2f",s/n);
}

void put(int v[],int n)
{
    for(int i =0;i<n;++i)
    {
        printf("%d ",v[i]);
    }
}

int v[1010],i=0,x;
double s=0;
int main()
{
    do
    {
        scanf("%d",&x);
        if(x==1) avg(s,i);
        if(x==0) put(v,i);
        else if(x>1)
        {
            v[i] = x;
            s+=v[i];
            ++i;
        }




    }while(x!=-1);



    return 0;
}