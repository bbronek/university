#include <iostream>
#include <string>
using namespace std;

int main(void) {
    int count, occurrences = 0;
    string words[100], target;
    cin >> count;
    for (int i = 0; i < count; ++i) {
        cin >> words[i];
    }
    cin >> target;
    for (int i = 0; i < count; ++i) {
        if (words[i] == target)
            occurrences += 1;
    }

    cout << occurrences;

    return 0;
}
