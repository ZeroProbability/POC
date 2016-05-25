// Exercise 4-14. Define a macro swap(t,x,y) that interchanges two 
// arguments of type t .
//
#include <stdio.h>

#define swap(t,x,y) t temp=x; x=y; y=temp;

int main() {
  int x, y;
  x=10; y=5;
  
  printf("x=%d, y=%d\n",x,y);
  swap(int, x, y);
  printf("x=%d, y=%d\n",x,y);

  return 0;
}
