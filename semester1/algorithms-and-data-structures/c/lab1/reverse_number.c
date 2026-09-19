#include <stdio.h>

void print_reversed(int n) {
  if (n == 0)
    printf("0");
  while (n) {
    printf("%d", n % 10);
    n /= 10;
  }
}

int n;
int main() {
  scanf("%d", &n);
  print_reversed(n);

  return 0;
}