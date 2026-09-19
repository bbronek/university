#include <stdio.h>

int main(void) {
    int lower = 0, upper = 0, count = 0, value = 0, distance = 0;
    if (scanf("%d%d", &lower, &upper) != 2)
        return 1;
    if (scanf("%d", &count) != 1)
        return 1;
    for (int i = 0; i < count; ++i) {
        if (scanf("%d", &value) != 1)
            return 1;
        if (value < lower)
            distance += lower - value;
        if (value > upper)
            distance += value - upper;
        if (value >= lower && value <= upper)
            distance = 0;
    }
    printf("%d", distance);

    return 0;
}
