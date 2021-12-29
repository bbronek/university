#include <stdio.h>

void  scal(int A[],int p,int q,int r)
{
    int n =q-p+1;
    int m = r-q;
    int B[n+1];
    int C[m+1];
    for(int i =1;i<=n;++i)
    {
        B[i] = A[i+p-1];
    }
    for(int j=1;j<=m;++j)
    {
        C[j] = A[q+j];
    }
    B[n+1] = __INT32_MAX__;
    C[m+1] = __INT32_MAX__;
    int i =1,j=1;
    for(int k=p;k<=r;++k)
    {
        if(B[i]<=C[j])
        {
            A[k] = B[i];
            i = i+1;
        }
        else
        {
            A[k] = C[j];
            j = j+1;
        }
    }
}
void sortScal(int A[],int p,int r)
{
    if (p<r)
    {
        int q = (p+r)/2;
        sortScal(A,p,q);
        sortScal(A,q+1,r);
        scal(A,p,q,r);
    }
}


int A[100000],n;
int main()
{
    scanf("%d",&n);
    for(int i =0;i<n;++i)
    {
        scanf("%d",&A[i]);
    }
    sortScal(A,0,n-1);
    for(int i =0 ;i<n;++i)
    {
        printf("%d ",A[i]);
    }



    return 0;
}