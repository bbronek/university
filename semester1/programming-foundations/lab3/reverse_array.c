#include <stdio.h>

int main(void) {
    int length = 0;
    if (scanf("%d", &length) != 1)
        return 1;
    if (length <= 0 || length > 1000000)
        return 1;
    int values[length];
    for (int i = 0; i < length; ++i) {
        if (scanf("%d", &values[i]) != 1)
            return 1;
    }
    for (int i = length - 1; i >= 0; --i) {
        printf("%d", values[i]);
    }

    return 0;
}
