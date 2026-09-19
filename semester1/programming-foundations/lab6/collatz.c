#include <stdio.h>

int even_steps = 0, odd_steps = 0;
void collatz(int value) {

    while (value != 1) {
        if (!(value % 2)) {
            even_steps += 1;
            value /= 2;
        } else {
            odd_steps += 1;
            value = 3 * value + 1;
        }
    }
}

int main(void) {

    int number = 0;
    do {
        even_steps = 0;
        odd_steps = 0;
        if (scanf("%d", &number) != 1)
            return 1;
        if (number <= 0)
            break;
        collatz(number);
        if ((even_steps + odd_steps) <= 15) {
            printf("%s %d %d", "YES", even_steps, odd_steps);
        } else
            printf("NO");

    } while (1);

    return 0;
}
