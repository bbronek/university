#include <limits.h>
#include <stdio.h>

int main(void) {
  int count, maximum = INT_MIN, maximum_index = 0;
  if (scanf("%d", &count) != 1 || count <= 0)
    return 1;
  for (int index = 1; index <= count; ++index) {
    int value;
    if (scanf("%d", &value) != 1)
      return 1;
    if (value > maximum || maximum_index == 0) {
      maximum = value;
      maximum_index = index;
    }
  }
  printf("%d %d\n", maximum, maximum_index);
  return 0;
}
