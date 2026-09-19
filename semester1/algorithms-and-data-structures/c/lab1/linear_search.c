#include <stdio.h>

int linear_search(int values[], int length, int target) {
    for (int i = 0; i < length; ++i) {
        if (values[i] == target)
            return i + 1;
    }
    return 0;
}

int main(void) {
    int case_count = 0, length = 0, target = 0;
    if (scanf("%d", &case_count) != 1)
        return 1;
    for (int i = 0; i < case_count; ++i) {
        if (scanf("%d", &length) != 1)
            return 1;
        if (length <= 0 || length > 1000000)
            return 1;
        int values[length];
        for (int j = 0; j < length; ++j) {
            if (scanf("%d", &values[j]) != 1)
                return 1;
        }
        if (scanf("%d", &target) != 1)
            return 1;
        int index = linear_search(values, length, target);
        if (index)
            printf("%d", index);
        else
            printf("NOT FOUND");
    }

    return 0;
}
