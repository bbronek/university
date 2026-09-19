#include <stdio.h>

int is_perfect(int n) {
  if (n < 2)
    return 0;
  int s = 1;
  for (int i = 2; i < n; ++i) {
    if (!(n % i))
      s += i;
  }
  return (s == n);
}

int n;
int main() {
  scanf("%d", &n);
  if (is_perfect(n))
    printf("yes");
  else
    printf("no");

  return 0;
}
