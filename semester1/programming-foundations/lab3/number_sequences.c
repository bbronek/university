#include <stdio.h>

int l, p, b;
char z;
int main(void) {
  scanf("%d%d %c", &l, &p, &z);
  b = l % 2;
  if (z == 'e') {
    if (!(b)) {
      for (int i = l; i <= p; i += 2) {
        printf("%d", i);
      }
    }
    if (b) {
      for (int i = l + 1; i <= p; i += 2) {
        printf("%d", i);
      }
    }
  }
  if (z == 'o') {
    if (!(b)) {
      for (int i = l + 1; i <= p; i += 2) {
        printf("%d", i);
      }
    }
    if (b) {
      for (int i = l; i <= p; i += 2) {
        printf("%d", i);
      }
    }
  }

  return 0;
}