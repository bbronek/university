#include <stdio.h>

void print_boom(int count) {
    printf("B");
    for (int i = 0; i < count; ++i) {
        printf("I");
    }
    printf("G B");
    for (int i = 0; i < count; ++i) {
        printf("O");
    }
    printf("M");
    for (int i = 0; i < count; ++i) {
        printf("!");
    }
}
int main(void) {
    int count = 0, size = 0;
    if (scanf("%d", &count) != 1)
        return 1;
    for (int i = 0; i < count; ++i) {
        if (scanf("%d", &size) != 1)
            return 1;
        print_boom(size);
    }

    return 0;
}
