#include <stdio.h>

void print_boom(int n) {
  printf("B");
  for (int i = 0; i < n; ++i) {
    printf("I");
  }
  printf("G B");
  for (int i = 0; i < n; ++i) {
    printf("O");
  }
  printf("M");
  for (int i = 0; i < n; ++i) {
    printf("!");
  }
}
int main(void) {
  int n, x;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d", &x);
    print_boom(x);
  }

  return 0;
}