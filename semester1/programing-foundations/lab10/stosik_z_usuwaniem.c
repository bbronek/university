#include <stdio.h>
#include <stdlib.h>

struct elem {
    int val;
    struct elem* ptr;
};

struct stack {
    int size;
    struct elem* head;
};

struct stack *create_empty_stack() {
    struct stack *empty_stack = malloc(sizeof(struct stack));
    if (empty_stack == NULL) {
        fprintf(stderr, "Memory not allocated. Stack not constructed.");
        exit(1);
    }
    empty_stack->size = 0;
    empty_stack->head = NULL;
    return empty_stack;
}

void push(struct stack* stack_ptr, int num) {
    struct elem *element = malloc(sizeof(struct elem));
    element->val = num;
    element->ptr = stack_ptr->head;
    stack_ptr->head = element;
    stack_ptr->size += 1;
}
/* PRZED : NULL <- 1 <- 2 <- head
   PO : NULL <- 1 <- 2 <- 3 <- head */

/* PRZED: NULL <- head                                                               */
/* PO:    NULL <- 3 <- head */

void remove_all(struct stack *stack_ptr,int num) {
    struct elem *iter = stack_ptr->head;
    struct elem *prev = NULL;
    while(iter != NULL)
    {
        if(iter->val == num){
            stack_ptr->size -=1;
            if(prev == NULL){
                stack_ptr->head = iter->ptr;
            }
            else{
                prev->ptr = iter->ptr;
            }
            struct elem *tmp = iter;
            iter = iter->ptr;
            free(tmp);
        }
        else{
            prev = iter;
            iter = iter->ptr;
        }

    }

}
int pop(struct stack* stack_ptr) {
    struct elem *tmp_element = stack_ptr->head;
    stack_ptr->head = tmp_element->ptr;
    int popped_num = tmp_element->val;
    free(tmp_element);
    stack_ptr->size -= 1;
    return popped_num;
}

void print_stack_elements(struct stack *stack_ptr) {
    struct elem *iter = stack_ptr->head;
    while (iter != NULL) {
        printf("%d ", iter->val);
        iter = iter->ptr;
    }
}

_Bool empty(struct stack *stack_ptr) {
    if (stack_ptr->size == 0) {
        printf("empty");
        return 1;
    } else {
        return 0;
    }
}

_Bool full(struct stack *stack_ptr) {
    if (stack_ptr->size == 100) {
        printf("full");
        return 1;
    } else {
        return 0;
    }
}

int main() {
    struct stack *stack_ptr = create_empty_stack();
    int num_of_operations;
    scanf("%d\n", &num_of_operations);
    for (int i = 0; i < num_of_operations; i++) {
        char operation;
        scanf("%c", &operation);
        if (operation == '+') {
            int num;
            scanf(" %d\n", &num);
            if (full(stack_ptr) == 0) {
                push(stack_ptr, num);
            }
        } else if (operation == '-'){
            scanf("\n");
            if (empty(stack_ptr) == 0) {
                int popped_num = pop(stack_ptr);
                printf("%d\n", popped_num);
            }
        }else if (operation == 'd'){
            int num;
            scanf(" %d\n",&num);
            remove_all(stack_ptr, num);
        }
    }
    print_stack_elements(stack_ptr);

    return 0;
}
