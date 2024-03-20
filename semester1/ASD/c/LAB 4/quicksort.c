#include <stdio.h>

void swap(int *a,int*b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int podzial(int A[],int p,int r)
{
    int x=A[r];
    int i = p-1;
    for (int j = p;j<r;++j)
    {
        if(A[j]<=x)
        {
            i = i +1;
            swap(&A[i],&A[j]);

        }
    }
    swap(&A[i+1],&A[r]);
    return i+1;

}
void quickSort(int A[],int p,int r)
{
    if (p<r)
    {
        int q = podzial(A,p,r);
        quickSort(A,p,q-1);
        quickSort(A,q+1,r);
    }
}

int A[1000],n;
int main()
{
    scanf("%d",&n);
    for(int i =0;i<n;++i)
    {
        scanf("%d",&A[i]);
    }
    quickSort(A,0,n-1);
    for(int i =0 ;i<n;++i)
    {
        printf("%d ",A[i]);
    }


    return 0;
}
