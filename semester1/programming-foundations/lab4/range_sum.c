#include <stdio.h>

int sum(int values[], int start, int end) {
    int total = 0;
    for (int i = start - 1; i <= end - 1; ++i) {
        total += values[i];
    }
    return total;
}

int main(void) {
    int length = 0, query_count = 0, start = 0, end = 0;
    if (scanf("%d", &length) != 1)
        return 1;
    if (length <= 0 || length > 1000000)
        return 1;
    int values[length];
    for (int i = 0; i < length; ++i) {
        if (scanf("%d", &values[i]) != 1)
            return 1;
    }
    if (scanf("%d", &query_count) != 1)
        return 1;
    for (int i = 0; i < query_count; ++i) {
        if (scanf("%d%d", &start, &end) != 2)
            return 1;
        printf("%d", sum(values, start, end));
    }

    return 0;
}
