#include <stdio.h>

long long fib(long long n) {
    if (n == 0)
        return 0;
    long long a = 0;
    long long b = 1;
    for (int i = 2; i <= n; ++i) {
        b += a;
        a = b - a;
    }
    return b;
}

int main(void) {
    long long n = 0;
    if (scanf("%lld", &n) != 1)
        return 1;
    printf("%lld", fib(n));

    return 0;
}
