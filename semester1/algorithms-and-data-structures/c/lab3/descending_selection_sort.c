#include <stdio.h>

void swap(int *a, int *b) {
    int values = 0;

    values = *b;
    *b = *a;
    *a = values;
}

int maximum_index(int values[], int i, int length) {
    int largest_index = i;

    for (int j = i + 1; j < length; j++)
        if (values[j] > values[largest_index])
            largest_index = j;
    return largest_index;
}

void sort(int values[], int length) {
    int largest = 0;
    for (int i = 0; i < length; ++i) {
        largest = maximum_index(values, i, length);
        swap(&values[largest], &values[i]);
    }
}

void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d", arr[i]);
}

int main(void) {
    int length = 0, values[100];
    if (scanf("%d", &length) != 1 || length < 0 || length > 100)
        return 1;
    for (int i = 0; i < length; ++i) {
        if (scanf("%d ", &values[i]) != 1)
            return 1;
    }
    sort(values, length);
    print_array(values, length);

    return 0;
}
