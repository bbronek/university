#include <stdio.h>

int main(void) {
    int case_count = 0;
    if (scanf("%d", &case_count) != 1)
        return 1;

    while (case_count--) {

        int number = 0, step = 0;

        if (scanf("%d %d", &number, &step) != 2 || number < 0 || step <= 0)
            return 1;
        int result = 1;

        for (int i = number; i >= step; i -= step) {
            result *= i;
        }
        printf("%d\n", result);
    }
    return 0;
}
