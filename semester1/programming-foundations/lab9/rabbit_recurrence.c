#include <stdio.h>
#include <stdlib.h>

long long rabbit_population(long long month, long long cache[]) {
    if (cache[month] != -1)
        return cache[month];
    if (month <= 4)
        return 1;
    if (month == 5)
        cache[month] =
            rabbit_population(month - 1, cache) + 3 * rabbit_population(month - 4, cache);
    else
        cache[month] = rabbit_population(month - 1, cache) +
                       3 * rabbit_population(month - 4, cache) -
                       2 * rabbit_population(month - 5, cache);
    return cache[month];
}

int main(void) {

    int case_count = 0;
    long long *cache, month = 0;
    if (scanf("%d", &case_count) != 1)
        return 1;
    cache = (long long *)malloc((101) * sizeof(long long));
    for (int i = 0; i <= 100; ++i) {
        cache[i] = -1;
    }

    for (int i = 0; i < case_count; ++i) {
        if (scanf("%lld", &month) != 1)
            return 1;
        printf("%lld", rabbit_population(month, cache));
    }

    return 0;
}
