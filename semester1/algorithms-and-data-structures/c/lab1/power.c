#include <stdio.h>

int power(int n, int m) {
  int w = 1;
  for (int i = 0; i < m; ++i) {
    w *= n;
  }
  return (w);
}

int n, m;
int main() {
  scanf("%d%d", &n, &m);
  printf("%d", power(n, m));

  return 0;
}