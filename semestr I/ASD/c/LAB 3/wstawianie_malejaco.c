#include <stdio.h>

void swap(int *a, int *b)
{
    int t;

    t  = *b;
    *b = *a;
    *a = t;
}

int max_elem(int t[] ,int i,int n)
{
    int max_idx = i;

    for (int j = i+1; j < n; j++)
        if (t[j] > t[max_idx])
            max_idx = j;
    return max_idx;
}

void sort(int t[],int n)
{
    int max;
    for(int i =0 ; i <n ;++i)
    {
        max = max_elem(t,i,n);
        swap(&t[max],&t[i]);
    }

}

void printArray(int arr[], int size)
{
    for (int i=0; i < size; i++)
        printf("%d",arr[i]);
}

int n,v[100];
int main()
{
    scanf("%d",&n);
    for(int i =0 ;i<n;++i)
    {
        scanf("%d ",&v[i]);
    }
    sort(v,n);
    printArray(v,n);

    return 0;
}