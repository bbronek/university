#include <stdio.h>

char parity;
int main(void) {
    int start = 0, end = 0, is_odd = 0;
    if (scanf("%d%d %c", &start, &end, &parity) != 3)
        return 1;
    is_odd = start % 2;
    if (parity == 'e') {
        if (!(is_odd)) {
            for (int i = start; i <= end; i += 2) {
                printf("%d", i);
            }
        }
        if (is_odd) {
            for (int i = start + 1; i <= end; i += 2) {
                printf("%d", i);
            }
        }
    }
    if (parity == 'o') {
        if (!(is_odd)) {
            for (int i = start + 1; i <= end; i += 2) {
                printf("%d", i);
            }
        }
        if (is_odd) {
            for (int i = start; i <= end; i += 2) {
                printf("%d", i);
            }
        }
    }

    return 0;
}
