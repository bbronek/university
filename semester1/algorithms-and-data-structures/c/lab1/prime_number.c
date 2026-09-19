#include <stdio.h>

int is_prime(int count) {
    if (count < 2)
        return 0;
    for (int i = 2; i <= count / i; ++i) {
        if (!(count % i))
            return 0;
    }
    return 1;
}

int main(void) {
    int count = 0, value = 0;
    if (scanf("%d", &count) != 1)
        return 1;
    for (int i = 0; i < count; ++i) {
        if (scanf("%d", &value) != 1)
            return 1;
        if (is_prime(value))
            printf("PRIME");
        else
            printf("NOT PRIME");
    }

    return 0;
}
