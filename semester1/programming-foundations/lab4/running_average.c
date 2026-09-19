#include <stdio.h>

void print_average(double total, int n) {
    if (n > 0)
        printf("%.2f", total / n);
}

void print_values(int values[], int n) {
    for (int count = 0; count < n; ++count) {
        printf("%d ", values[count]);
    }
}

int main(void) {
    double total = 0;
    int values[1010], count = 0, command = 0;
    do {
        if (scanf("%d", &command) != 1)
            return 1;
        if (command == 1)
            print_average(total, count);
        if (command == 0)
            print_values(values, count);
        else if (command > 1) {
            if (count == 1010)
                return 1;
            values[count] = command;
            total += values[count];
            ++count;
        }

    } while (command != -1);

    return 0;
}
