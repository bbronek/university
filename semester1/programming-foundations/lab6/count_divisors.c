#include <stdio.h>
#include <stdlib.h>

int count_divisors(int v[], int x, int n) {
  int l = 0;
  for (int i = 0; i < n; ++i) {
    if (v[i] != 0 && !(x % v[i]))
      l += 1;
  }
  return l;
}

int n, m, *v, x;
int main() {

  scanf("%d", &n);
  v = malloc(n * sizeof(int));

  for (int i = 0; i < n; ++i) {
    scanf("%d", &v[i]);
  }

  scanf("%d", &m);

  for (int i = 0; i < m; ++i) {
    scanf("%d", &x);
    printf("%d", count_divisors(v, x, n));
  }

  return 0;
}