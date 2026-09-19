#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int values[], int left, int right) {
    int pivot = values[right];
    int i = left - 1;
    for (int j = left; j < right; ++j) {
        if (values[j] <= pivot) {
            i = i + 1;
            swap(&values[i], &values[j]);
        }
    }
    swap(&values[i + 1], &values[right]);
    return i + 1;
}
void quick_sort(int values[], int left, int right) {
    if (left < right) {
        int middle = partition(values, left, right);
        quick_sort(values, left, middle - 1);
        quick_sort(values, middle + 1, right);
    }
}

int main(void) {
    int values[1000], length = 0;
    if (scanf("%d", &length) != 1 || length < 0 || length > 1000)
        return 1;
    for (int i = 0; i < length; ++i) {
        if (scanf("%d", &values[i]) != 1)
            return 1;
    }
    quick_sort(values, 0, length - 1);
    for (int i = 0; i < length; ++i) {
        printf("%d ", values[i]);
    }

    return 0;
}
