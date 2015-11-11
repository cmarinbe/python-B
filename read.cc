#include <fstream>
#include <iostream>
#include <iterator>
#include <sstream>
#include <vector>

struct B { double m, merr, pt, p; };

auto readline(const std::string& line) {
  std::stringstream ss{line};
  std::string token{};
  auto data = std::vector<double>{};
  while (std::getline(ss, token, ',')) {
    data.push_back(std::stod(token));
  }
  return B{data[0], data[1], data[2], data[3]};
}

auto read(const std::string& filename) {
  auto ifs = std::ifstream{filename};
  auto res = std::vector<B>{};
  auto line = std::string{};
  ifs >> line;
  while (ifs >> line) {
    res.push_back(readline(line));
  }
  return res;
}

int main() {
  auto bs = read("B.txt");
  for (const auto& b : bs) {
    std::cout << b.m << '\n';
  }
}
