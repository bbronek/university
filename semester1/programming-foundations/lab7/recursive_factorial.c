#include <stdio.h>

int factorial(int number) {
    if (number < 2)
        return 1;
    return number * factorial(number - 1);
}

int main(void) {
    int number = 0;
    if (scanf("%d", &number) != 1)
        return 1;
    printf("%d", factorial(number));

    return 0;
}
