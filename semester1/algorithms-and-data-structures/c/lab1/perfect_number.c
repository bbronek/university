#include <stdio.h>

int is_perfect(int number) {
    if (number < 2)
        return 0;
    int divisor_sum = 1;
    for (int i = 2; i < number; ++i) {
        if (!(number % i))
            divisor_sum += i;
    }
    return (divisor_sum == number);
}

int main(void) {
    int number = 0;
    if (scanf("%d", &number) != 1)
        return 1;
    if (is_perfect(number))
        printf("yes");
    else
        printf("no");

    return 0;
}
