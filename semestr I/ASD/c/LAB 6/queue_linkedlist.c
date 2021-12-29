#include <stdio.h>
#include <stdlib.h>

struct Node
{
    struct elem* head;
};

struct elem
{
    int val;
    struct elem* next;
};

struct Node *create_empty_queue()
{
    struct Node *eq = malloc(sizeof(struct Node));
    if(eq == NULL)
    {
        fprintf(stderr, "Memory not allocated. Stack not constructed.");
        exit(1);
    }
    eq->head = NULL;
    return eq;

}



void enqueue(struct Node* root,int x)
{
    struct elem* new = malloc(sizeof(struct elem));
    struct elem* temp = root->head;
    int i =1;
    if (x == i)
    {
        new->val = x;
        new->next = root->head;
        root->head = new;
    }
    else
    {

        while(temp->next != NULL && i!=x-1)
        {
            temp = temp->next;
            ++i;

        }

        new->next = temp ->next;
        temp->next = new;
        new->val = x;


    }




}
int deleteFirst(struct Node* stack_ptr) {

    struct elem *tmp_element = stack_ptr->head;
    int popped_num = tmp_element->val;
    stack_ptr->head = tmp_element->next;
    return popped_num;
}



int d,n,var,v,c=0;
int main()
{
    struct Node* head = create_empty_queue();
    scanf("%d",&d);
    for(int i =0;i<d;++i)
    {
        scanf("%d",&n);
        for(int j =0;j<n;++j)
        {
            scanf("%d",&var);
            if(var!=0)
            {
                enqueue(head,var);

            }

            else
            {
                v= deleteFirst(head);
                c++;
            }

            if(c==1)
            {
                printf("%d", v);

                c = 0;
            }



        }

    }
    return 0;
}

