#include <stdio.h>

// Exercise 2-7. Write a function invert(x,p,n) that returns x with the n bits 
// that begin at position p inverted (i.e., 1 changed into 0 and vice versa), 
// leaving the others unchanged.  

unsigned invert(unsigned x, int p, int n);

int main() {
  printf("%u", invert(127-32,4,3));
  return 0;
}

unsigned invert(unsigned x, int p, int n){
  int i=0,mask=0;
  for(i=0;i<n;i++) mask=(mask<<1)+1;

  mask=mask<<p;  // right shift p times 
  unsigned v1=x&~mask;
  unsigned v2=(~(x&mask)&mask);

  return v1|v2;
}

