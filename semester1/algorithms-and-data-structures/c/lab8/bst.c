#include <stdio.h>
#include <stdlib.h>

struct Node {
    int key;
    struct Node *left;
    struct Node *right;
} *root = NULL;

struct Node *insert(struct Node *root, int key) {
    if (root == NULL) {
        root = (struct Node *)malloc(sizeof(struct Node));
        root->key = key;
        root->left = root->right = NULL;
        return root;
    }

    if (key < root->key)
        root->left = insert(root->left, key);
    else if (key > root->key)
        root->right = insert(root->right, key);
    return root;
}

struct Node *search(int key) {
    struct Node *node = root;

    while (node != NULL) {
        if (key == node->key) {
            printf("1");
            return NULL;
        }

        else if (key < node->key) {
            printf("L");
            node = node->left;
        }

        else {
            printf("P");
            node = node->right;
        }
    }
    printf("0");
    return NULL;
}

int main(void) {
    int count = 0, value = 0, target = 0;

    if (scanf("%d", &count) != 1)
        return 1;
    if (scanf("%d", &value) != 1)
        return 1;
    root = insert(root, value);
    for (int i = 0; i < count - 1; ++i) {
        if (scanf("%d", &value) != 1)
            return 1;
        insert(root, value);
    }

    if (scanf("%d", &target) != 1)
        return 1;

    search(target);

    return 0;
}
