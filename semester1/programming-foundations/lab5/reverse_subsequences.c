#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int length = 0;
    int *array;
    if (scanf("%d", &length) != 1 || length < 1 || length > 1000000)
        return 1;
    array = malloc(length * sizeof(int));
    if (array == NULL)
        return 1;
    for (int i = 0; i < length; ++i) {
        if (scanf("%d", &array[i]) != 1)
            return 1;
    }
    int remainder = length % 3;
    for (int i = length - 1 - remainder; i >= 0; i -= 3) {
        printf("%d ", array[i]);
    }

    free(array);
    return 0;
}
