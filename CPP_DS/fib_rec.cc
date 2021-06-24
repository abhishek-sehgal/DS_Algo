#include <chrono>
#include <iostream>

using std::chrono::duration;
using std::chrono::duration_cast;
using std::chrono::high_resolution_clock;
using std::chrono::milliseconds;

int fib_rec(int n) {
  if (n < 2)
    return n;
  return fib_rec(n - 1) + fib_rec(n - 2);
}

int main() {
  auto t1 = high_resolution_clock::now();
  std::cout << fib_rec(2) << std::endl;
  std::cout << fib_rec(5) << std::endl;
  std::cout << fib_rec(10) << std::endl;
  std::cout << fib_rec(40) << std::endl;
  auto t2 = high_resolution_clock::now();
  duration<double, std::milli> ms_double = t2 - t1;
  std::cout << ms_double.count() << " ms" << std::endl;
  return 0;
}
