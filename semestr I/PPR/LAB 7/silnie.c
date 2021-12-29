#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    while (n--) {

        int a, b;

        scanf("%d %d", &a, &b);
        int w = 1;

        for (int i = a; i >= b; i -= b) {
            w *= i;
        }
        printf("%d\n", w);
    }
    return 0