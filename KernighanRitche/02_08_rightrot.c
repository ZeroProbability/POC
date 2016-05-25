#include <stdio.h>
#include <limits.h>

// Exercise 2-8. Write a function rightrot(x,n) that returns the value of the 
// integer x rotated to the right by n positions.

unsigned rightrot(unsigned x, int n);

int main() {
  printf("%u", rightrot(1,30));
  return 0;
}

unsigned rightrot(unsigned x, int n) {
  int i;
  for(i=0;i<n;i++) {
    int last_bit=x&1;
    x>>=1;
    if(last_bit) 
    x|=(~((unsigned)INT_MAX));
  }
  return x;
}

