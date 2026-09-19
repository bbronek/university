#include <iostream>
using namespace std;

int rabbit_population(int m) {
  return m < 3 ? 1 : rabbit_population(m - 1) + 2 * rabbit_population(m - 3);
}

int main() {
  int t;
  cin >> t;
  while (t > 0) {
    int m;
    cin >> m;
    cout << rabbit_population(m) << endl;
    t--;
  }
  return 0;
}