#include <limits.h>
#include <stdio.h>

int main(void) {
  int count, maximum = INT_MIN, occurrences = 0;
  if (scanf("%d", &count) != 1 || count < 1)
    return 1;
  for (int index = 0; index < count; ++index) {
    int value;
    if (scanf("%d", &value) != 1)
      return 1;
    if (value > maximum) {
      maximum = value;
      occurrences = 1;
    } else if (value == maximum) {
      ++occurrences;
    }
  }
  printf("%d\n", occurrences);
  return 0;
}
