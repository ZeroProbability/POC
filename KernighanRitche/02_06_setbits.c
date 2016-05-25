#include <stdio.h>

// Exercise 2-6. Write a function setbits(x,p,n,y) that returns x with the n 
// bits that begin at position p set to the rightmost n bits of y , leaving the
// other bits unchanged.

int setbits(int x, int p, int n, int y);

int main() {
  printf("%d", setbits(127,4,3,5));
  return 0;
}

int setbits(int x, int p, int n, int y){
  int i=0,mask=0;
  for(i=0;i<n;i++) mask=(mask<<1)+1;
  y=y&mask;      // remove all other bits other than masked bit

  mask=mask<<p;  // right shift p times 
  y=y<<p;  // right shift y's bits too

  return ((x&~mask) | y);
}
