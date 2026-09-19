#include <stdio.h>

void merge(int values[], int left, int middle, int right) {
  int length = right - left + 1;
  int merged[length];
  int first = left, second = middle + 1;
  for (int index = 0; index < length; ++index) {
    if (first <= middle &&
        (second > right || values[first] <= values[second])) {
      merged[index] = values[first++];
    } else {
      merged[index] = values[second++];
    }
  }
  for (int index = 0; index < length; ++index)
    values[left + index] = merged[index];
}
void merge_sort(int A[], int p, int r) {
  if (p < r) {
    int q = (p + r) / 2;
    merge_sort(A, p, q);
    merge_sort(A, q + 1, r);
    merge(A, p, q, r);
  }
}

int A[100000], n;
int main() {
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d", &A[i]);
  }
  merge_sort(A, 0, n - 1);
  for (int i = 0; i < n; ++i) {
    printf("%d ", A[i]);
  }

  return 0;
}