#include <stdio.h>

int gcd(int a, int b) {
    while (a != b)
        if (a < b)
            b -= a;
        else
            a -= b;
    return a;
}

int main(void) {
    int command = 0, a = 0, b = 0;
    int total = 0;
    if (scanf("%d", &command) != 1)
        return 1;
    a = command;
    if (scanf(" %d ", &command) != 1)
        return 1;
    b = command;
    do {
        if (scanf(" %d", &command) != 1)
            return 1;
        if (command == 1 && a && b) {
            total += gcd(a, b);

        } else {
            b = a;
            a = command;
        }

    } while (command != 0);

    printf("%d", total);

    return 0;
}
