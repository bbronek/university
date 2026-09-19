#include <stdio.h>

int power(int base, int exponent) {
    int result = 1;
    for (int i = 0; i < exponent; ++i) {
        result *= base;
    }
    return (result);
}

int main(void) {
    int base = 0, exponent = 0;
    if (scanf("%d%d", &base, &exponent) != 2)
        return 1;
    printf("%d", power(base, exponent));

    return 0;
}
