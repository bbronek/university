#include <iostream>
#include <string>

using namespace std;

string reversed_word;
void reverse_word(string word) {
  int length = word.length();

  for (int i = 0; i < length; i++) {
    reversed_word += word[length - i - 1];
  }
}

int n;
int main() {
  string word;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    reversed_word = "";
    cin >> word;
    reverse_word(word);
    if (word == reversed_word)
      cout << word << "==" << reversed_word;
    else
      cout << word << "!=" << reversed_word;
  }

  return 0;
}