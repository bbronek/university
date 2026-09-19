#include <stdio.h>

int is_odd(int case_count) {
    if (case_count % 2)
        return 1;
    return 0;
}

int main(void) {
    int case_count = 0, rows = 0, columns = 0, value = 0;
    if (scanf("%d", &case_count) != 1)
        return 1;
    for (int i = 0; i < case_count; ++i) {
        if (scanf("%d%d", &rows, &columns) != 2)
            return 1;
        for (int j = 1; j <= rows; ++j) {
            for (int k = 1; k <= columns; ++k) {
                if (scanf("%d", &value) != 1)
                    return 1;
                if (is_odd(value))
                    printf("%d (%d,%d)", value, k, j);
            }
        }
    }

    return 0;
}
