#include <stdio.h>
#include <stdlib.h>

int heapsize =0;
typedef struct elem
{
    int id;
    int priorytet;
} elem;

elem A[1000000];

void swap(elem *x, elem *y)
{
    elem temp = *x;
    *x = *y;
    *y = temp;
}

int PARENT(int i)
{
    return i/2;
}

int LEFT(int i)
{
    return 2*i;
}

int RIGHT(int i)
{
    return 2*i+1;
}

int MAX_HEAPIFY(elem A[],int i)
{
    int X = i;


    if ( ((RIGHT(i) <= heapsize) && (A[RIGHT(i)].priorytet > A[X].priorytet)) || ((RIGHT(i) <= heapsize) && (A[RIGHT(i)].priorytet == A[X].priorytet) && ( A[RIGHT(i)].id < A[X].id)))
        X = RIGHT(i);
    if ( ((LEFT(i) <= heapsize) && (A[LEFT(i)].priorytet > A[X].priorytet)) || ((LEFT(i) <= heapsize) && (A[LEFT(i)].priorytet == A[X].priorytet) && (A[LEFT(i)].id < A[X].id)))
        X = LEFT(i);
    if (X!=i)
    {
        swap(&A[X],&A[i]);
        MAX_HEAPIFY(A,X);
    }

}

int HEAP_EXTRACT_MAX(elem A[])
{

    elem Max = A[1];
    A[1] = A[heapsize];
    heapsize -=1;
    MAX_HEAPIFY(A,1);
    return Max.id;
}

void HEAP_INCREASE_KEY(elem A[],int i,int key)
{
    if (key<A[i].priorytet)
    {
        printf("ERROR");
    }

    else
    {
        A[i].priorytet = key;
        while(i>1 && ((A[i].priorytet > A[PARENT(i)].priorytet) ))
        {
            swap(&A[i],&A[PARENT(i)]);
            i = PARENT(i);
        }


    }

}

void MAX_HEAP_INSERT(elem A[],int key,int id)
{

    heapsize +=1;
    A[heapsize].priorytet = key;
    A[heapsize].id =id;
    HEAP_INCREASE_KEY(A,heapsize,key);

}

int n,x,id =0;
int main()
{

    scanf("%d",&n);
    for(int i =0;i<n;++i)
    {
        scanf("%d",&x);
        if(x == 0 && heapsize>0)
        {

            printf("%d\n",HEAP_EXTRACT_MAX(A));

        }
        else if(x!=0)
        {
            id +=1;
            MAX_HEAP_INSERT(A,x,id);
        }


    }




    return 0;
}

