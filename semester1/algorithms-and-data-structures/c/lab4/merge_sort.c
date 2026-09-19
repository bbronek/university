#include <stdio.h>

void merge(int values[], int left, int middle, int right) {
    int length = right - left + 1;
    int merged[length];
    int first = left, second = middle + 1;
    for (int index = 0; index < length; ++index) {
        if (first <= middle && (second > right || values[first] <= values[second])) {
            merged[index] = values[first++];
        } else {
            merged[index] = values[second++];
        }
    }
    for (int index = 0; index < length; ++index)
        values[left + index] = merged[index];
}
void merge_sort(int values[], int left, int right) {
    if (left < right) {
        int middle = (left + right) / 2;
        merge_sort(values, left, middle);
        merge_sort(values, middle + 1, right);
        merge(values, left, middle, right);
    }
}

int main(void) {
    int values[100000], length = 0;
    if (scanf("%d", &length) != 1 || length < 0 || length > 100000)
        return 1;
    if (length <= 0 || length > 1000000)
        return 1;
    for (int i = 0; i < length; ++i) {
        if (scanf("%d", &values[i]) != 1)
            return 1;
    }
    merge_sort(values, 0, length - 1);
    for (int i = 0; i < length; ++i) {
        printf("%d ", values[i]);
    }

    return 0;
}
