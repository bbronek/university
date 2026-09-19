#include <iostream>
#include <string>
#include <vector>

int main() {
  std::vector<int> values;
  std::string command;
  bool failed = false;
  while (std::cin >> command && command != "END") {
    if (command == "PUSH") {
      int value;
      if (!(std::cin >> value))
        return 1;
      if (values.size() == 100)
        failed = true;
      else
        values.push_back(value);
    } else if (command == "POP") {
      if (values.empty())
        failed = true;
      else
        values.pop_back();
    } else {
      return 1;
    }
  }
  if (failed) {
    std::cout << "error\n";
    return 0;
  }
  while (!values.empty()) {
    std::cout << values.back() << '\n';
    values.pop_back();
  }
}
