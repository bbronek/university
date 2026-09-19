#include <stdio.h>

void print_reversed(int number) {
    if (number == 0)
        printf("0");
    while (number) {
        printf("%d", number % 10);
        number /= 10;
    }
}

int main(void) {
    int number = 0;
    if (scanf("%d", &number) != 1)
        return 1;
    print_reversed(number);

    return 0;
}
