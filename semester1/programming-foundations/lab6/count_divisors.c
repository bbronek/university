#include <stdio.h>
#include <stdlib.h>

int count_divisors(int divisors[], int value, int divisor_count) {
    int count = 0;
    for (int i = 0; i < divisor_count; ++i) {
        if (divisors[i] != 0 && !(value % divisors[i]))
            count += 1;
    }
    return count;
}

int main(void) {
    int divisor_count = 0, query_count = 0, *divisors = 0, value = 0;

    if (scanf("%d", &divisor_count) != 1)
        return 1;
    if (divisor_count <= 0 || divisor_count > 1000000)
        return 1;
    divisors = malloc(divisor_count * sizeof(int));
    if (divisors == NULL)
        return 1;

    for (int i = 0; i < divisor_count; ++i) {
        if (scanf("%d", &divisors[i]) != 1)
            return 1;
    }

    if (scanf("%d", &query_count) != 1)
        return 1;

    for (int i = 0; i < query_count; ++i) {
        if (scanf("%d", &value) != 1)
            return 1;
        printf("%d", count_divisors(divisors, value, divisor_count));
    }

    free(divisors);
    return 0;
}
