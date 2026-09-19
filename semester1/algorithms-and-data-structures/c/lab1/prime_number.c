#include <stdio.h>

int is_prime(int n) {
  if (n < 2)
    return 0;
  for (int i = 2; i <= n / i; ++i) {
    if (!(n % i))
      return 0;
  }
  return 1;
}

int n, x;
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d", &x);
    if (is_prime(x))
      printf("PRIME");
    else
      printf("NOT PRIME");
  }

  return 0;
}
