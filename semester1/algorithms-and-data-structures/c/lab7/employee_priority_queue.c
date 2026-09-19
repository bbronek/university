#include <stdio.h>
#include <stdlib.h>

int heap_size = 0;
typedef struct Employee {
    int id;
    int priority;
} Employee;

Employee heap[1000001];

void swap(Employee *priority, Employee *y) {
    Employee temp = *priority;
    *priority = *y;
    *y = temp;
}

int parent(int i) { return i / 2; }

int left(int i) { return 2 * i; }

int right(int i) { return 2 * i + 1; }

void heapify(Employee heap[], int i) {
    int largest = i;

    if (((right(i) <= heap_size) && (heap[right(i)].priority > heap[largest].priority)) ||
        ((right(i) <= heap_size) && (heap[right(i)].priority == heap[largest].priority) &&
         (heap[right(i)].id < heap[largest].id)))
        largest = right(i);
    if (((left(i) <= heap_size) && (heap[left(i)].priority > heap[largest].priority)) ||
        ((left(i) <= heap_size) && (heap[left(i)].priority == heap[largest].priority) &&
         (heap[left(i)].id < heap[largest].id)))
        largest = left(i);
    if (largest != i) {
        swap(&heap[largest], &heap[i]);
        heapify(heap, largest);
    }
}

int extract_maximum(Employee heap[]) {

    Employee maximum = heap[1];
    heap[1] = heap[heap_size];
    heap_size -= 1;
    heapify(heap, 1);
    return maximum.id;
}

void increase_priority(Employee heap[], int i, int key) {
    if (key < heap[i].priority) {
        printf("ERROR");
    }

    else {
        heap[i].priority = key;
        while (i > 1 && (heap[i].priority > heap[parent(i)].priority ||
                         (heap[i].priority == heap[parent(i)].priority &&
                          heap[i].id < heap[parent(i)].id))) {
            swap(&heap[i], &heap[parent(i)]);
            i = parent(i);
        }
    }
}

void insert_employee(Employee heap[], int key, int id) {

    heap_size += 1;
    heap[heap_size].priority = key;
    heap[heap_size].id = id;
    increase_priority(heap, heap_size, key);
}

int main(void) {
    int count = 0, priority = 0, id = 0;

    if (scanf("%d", &count) != 1)
        return 1;
    for (int i = 0; i < count; ++i) {
        if (scanf("%d", &priority) != 1)
            return 1;
        if (priority == 0 && heap_size > 0) {

            printf("%d\n", extract_maximum(heap));

        } else if (priority != 0) {
            id += 1;
            insert_employee(heap, priority, id);
        }
    }

    return 0;
}
