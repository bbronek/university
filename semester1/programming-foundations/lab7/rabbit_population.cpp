#include <iostream>
using namespace std;

int rabbit_population(int month) {
    return month < 3 ? 1 : rabbit_population(month - 1) + 2 * rabbit_population(month - 3);
}

int main(void) {
    int case_count;
    cin >> case_count;
    while (case_count > 0) {
        int month;
        cin >> month;
        cout << rabbit_population(month) << endl;
        case_count--;
    }
    return 0;
}
