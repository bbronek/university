#include <limits.h>
#include <stdio.h>

int main(void) {
    int count = 0, largest = INT_MIN, second_largest = INT_MIN;
    if (scanf("%d", &count) != 1 || count < 2)
        return 1;
    for (int index = 0; index < count; ++index) {
        int value = 0;
        if (scanf("%d", &value) != 1)
            return 1;
        if (value >= largest) {
            second_largest = largest;
            largest = value;
        } else if (value > second_largest) {
            second_largest = value;
        }
    }
    printf("%d %d\n", largest, second_largest);
    return 0;
}
