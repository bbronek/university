#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int key;
    struct Node *left;
    struct Node *right;
}*root=NULL;


struct Node *Insert(struct Node *root,int key)
{
    if(root == NULL)
    {
        root=(struct Node*)malloc(sizeof(struct Node));
        root->key = key;
        root->left=root->right=NULL;
        return root;
    }

    if(key<root->key)
        root->left = Insert(root->left,key);
    else if(key > root->key)
        root->right = Insert(root->right,key);
    return root;


}

struct Node* Search(int key)
{
    struct Node *t=root;

    while(t!=NULL)
    {
        if(key == t->key)
        {
            printf("1");
            return NULL;
        }

        else if (key<t->key)
        {
            printf("L");
            t=t->left;
        }

        else
        {
            printf("P");
            t=t->right;
        }

    }
    printf("0");
    return NULL;
}

int n,x,s;
int main()
{

    scanf("%d",&n);
    scanf("%d",&x);
    root = Insert(root,x);
    for(int i=0;i<n-1;++i)
    {
        scanf("%d",&x);
        Insert(root,x);
    }

    scanf("%d",&s);

    Search(s);


    return 0;
}

