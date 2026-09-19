#include <stdio.h>
#include <stdlib.h>

struct Node {
    int value;
    struct Node *next;
};

int main(void) {
    struct Node *head = NULL, *tail = NULL;
    int batches = 0;
    if (scanf("%d", &batches) != 1 || batches < 0)
        return 1;
    for (int batch = 0; batch < batches; ++batch) {
        int count = 0;
        if (scanf("%d", &count) != 1 || count < 0)
            return 1;
        for (int index = 0; index < count; ++index) {
            int value = 0;
            if (scanf("%d", &value) != 1)
                return 1;
            if (value != 0) {
                struct Node *node = malloc(sizeof *node);
                if (node == NULL)
                    return 1;
                *node = (struct Node){value, NULL};
                if (tail != NULL)
                    tail->next = node;
                else
                    head = node;
                tail = node;
            } else if (head != NULL) {
                struct Node *node = head;
                printf("%d\n", node->value);
                head = node->next;
                if (head == NULL)
                    tail = NULL;
                free(node);
            } else {
                puts("empty");
            }
        }
    }
    while (head != NULL) {
        struct Node *node = head;
        head = head->next;
        free(node);
    }
    return 0;
}
