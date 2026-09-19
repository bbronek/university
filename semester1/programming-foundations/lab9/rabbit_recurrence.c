#include <stdio.h>
#include <stdlib.h>

long long rabbit_population(long long n, long long v[]) {
  if (v[n] != -1)
    return v[n];
  if (n <= 4)
    return 1;
  if (n == 5)
    v[n] = rabbit_population(n - 1, v) + 3 * rabbit_population(n - 4, v);
  else
    v[n] = rabbit_population(n - 1, v) + 3 * rabbit_population(n - 4, v) -
           2 * rabbit_population(n - 5, v);
  return v[n];
}

int main() {

  int t;
  long long *v, n;
  scanf("%d", &t);
  v = (long long *)malloc((101) * sizeof(long long));
  for (int i = 0; i <= 100; ++i) {
    v[i] = -1;
  }

  for (int i = 0; i < t; ++i) {
    scanf("%lld", &n);
    printf("%lld", rabbit_population(n, v));
  }

  return 0;
}