#include <stdio.h>

int binary_search(int values[], int length, int target) {
    int left = 0, right = length - 1, middle = 0;
    while (left <= right) {
        middle = (left + right) / 2;
        if (values[middle] == target)
            return middle + 1;
        if (values[middle] > target)
            right = middle - 1;
        else
            left = middle + 1;
    }
    return 0;
}

int main(void) {
    int values[100000], length = 0, query_count = 0, target = 0;
    if (scanf("%d", &length) != 1 || length < 0 || length > 100000)
        return 1;
    for (int i = 0; i < length; ++i) {
        if (scanf("%d", &values[i]) != 1)
            return 1;
    }
    if (scanf("%d", &query_count) != 1)
        return 1;
    for (int i = 0; i < query_count; ++i) {
        if (scanf("%d", &target) != 1)
            return 1;
        int index = binary_search(values, length, target);
        if (index)
            printf("%d", index);
        else
            printf("NOT FOUND");
    }

    return 0;
}
