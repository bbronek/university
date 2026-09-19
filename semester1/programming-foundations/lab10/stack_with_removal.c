#include <stdio.h>
#include <stdlib.h>

struct elem {
    int val;
    struct elem *ptr;
};

struct stack {
    int size;
    struct elem *head;
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

void push(struct stack *stack_ptr, int num) {
    struct elem *element = malloc(sizeof(struct elem));
    if (element == NULL) {
        perror("malloc");
        exit(EXIT_FAILURE);
    }
    element->val = num;
    element->ptr = stack_ptr->head;
    stack_ptr->head = element;
    stack_ptr->size += 1;
}
/* BEFORE : NULL <- 1 <- 2 <- head
   AFTER : NULL <- 1 <- 2 <- 3 <- head */

/* BEFORE: NULL <- head */
/* AFTER:    NULL <- 3 <- head */

void remove_all(struct stack *stack_ptr, int num) {
    struct elem *iter = stack_ptr->head;
    struct elem *prev = NULL;
    while (iter != NULL) {
        if (iter->val == num) {
            stack_ptr->size -= 1;
            if (prev == NULL) {
                stack_ptr->head = iter->ptr;
            } else {
                prev->ptr = iter->ptr;
            }
            struct elem *tmp = iter;
            iter = iter->ptr;
            free(tmp);
        } else {
            prev = iter;
            iter = iter->ptr;
        }
    }
}
int pop(struct stack *stack_ptr) {
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

int main(void) {
    struct stack *stack_ptr = create_empty_stack();
    int num_of_operations = 0;
    if (scanf("%d\n", &num_of_operations) != 1)
        return 1;
    for (int i = 0; i < num_of_operations; i++) {
        char operation;
        if (scanf("%c", &operation) != 1)
            return 1;
        if (operation == '+') {
            int num = 0;
            if (scanf(" %d\n", &num) != 1)
                return 1;
            if (full(stack_ptr) == 0) {
                push(stack_ptr, num);
            }
        } else if (operation == '-') {
            scanf("\n");
            if (empty(stack_ptr) == 0) {
                int popped_num = pop(stack_ptr);
                printf("%d\n", popped_num);
            }
        } else if (operation == 'd') {
            int num = 0;
            if (scanf(" %d\n", &num) != 1)
                return 1;
            remove_all(stack_ptr, num);
        }
    }
    print_stack_elements(stack_ptr);

    while (stack_ptr->head != NULL)
        pop(stack_ptr);
    free(stack_ptr);
    return 0;
}
