#include <stdio.h>

int main(void) {
    int length = 0, value = 0;
    if (scanf("%d", &length) != 1)
        return 1;
    int values[length + 1];
    if (!(length % 2)) {
        for (int i = 1; i <= length; ++i) {
            if (scanf("%d", &value) != 1)
                return 1;
            if (!(i % 2))
                values[i] = value;
        }
        for (int i = length; i >= 1; i -= 2) {
            printf("%d ", values[i]);
        }

    } else {
        for (int i = 1; i <= length; ++i) {
            if (scanf("%d", &value) != 1)
                return 1;
            if (!(i % 2))
                values[i] = value;
        }
        for (int i = length - 1; i >= 1; i -= 2) {
            printf("%d ", values[i]);
        }
    }

    return 0;
}
