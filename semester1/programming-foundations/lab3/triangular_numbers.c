#include <stdio.h>

long v[65537];
_Bool check(int x) {
    int l = 1, p = 65536;
    int sr = 0;
    while (l <= p) {
        sr = (l + p) / 2;
        if (v[sr] == x)
            return 1;
        if (v[sr] > x)
            p = sr - 1;
        else
            l = sr + 1;
    }
    return 0;
}

int main(void) {
    int n = 0, d = 0;

    long i = 1, j = 0;
    for (int u = 1; u <= 65536; ++u) {
        v[u] = i;
        j += 1;
        i += j;
    }

    if (scanf("%d", &n) != 1)
        return 1;

    for (int i = 0; i < n; ++i) {
        if (scanf("%d", &d) != 1)
            return 1;
        printf("%d", check(d));
    }
}
