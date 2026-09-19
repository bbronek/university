#include <deque>
#include <iostream>
#include <string>

int main() {
  std::deque<int> values;
  std::string command;
  bool failed = false;
  while (std::cin >> command && command != "END") {
    if (command == "ENQUEUE") {
      int value;
      if (!(std::cin >> value))
        return 1;
      if (values.size() == 10)
        failed = true;
      else
        values.push_back(value);
    } else if (command == "DEQUEUE") {
      if (values.empty())
        failed = true;
      else
        values.pop_front();
    } else {
      return 1;
    }
  }
  if (failed) {
    std::cout << "error\n";
    return 0;
  }
  while (!values.empty()) {
    std::cout << values.front() << '\n';
    values.pop_front();
  }
}
