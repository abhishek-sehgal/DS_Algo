#include <chrono>
#include <iostream>
#include <map>

using std::chrono::duration;
using std::chrono::duration_cast;
using std::chrono::high_resolution_clock;
using std::chrono::milliseconds;

int fib_memo(int n, std::map<int, int> *memo = NULL) {
  /**
   * Find the fibonacci number given an integer n using memoization
   */
  if (memo == NULL)
    memo = new std::map<int, int>();
  if (memo->find(n) != memo->end())
    return memo->at(n);
  if (n < 2)
    return n;
  (*memo)[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo);
  return memo->at(n);
}

int main() {

  auto t1 = high_resolution_clock::now();
  
  std::cout << fib_memo(2) << std::endl;
  std::cout << fib_memo(5) << std::endl;
  std::cout << fib_memo(10) << std::endl;
  std::cout << fib_memo(40) << std::endl;
  
  auto t2 = high_resolution_clock::now();
  
  duration<double, std::milli> ms_double = t2 - t1;
  
  std::cout << ms_double.count() << " ms" << std::endl;
  
  return 0;
}
