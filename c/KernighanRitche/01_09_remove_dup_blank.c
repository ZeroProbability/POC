#include <stdio.h>

// Exercise 1-9. Write a program to copy its input to its output, replacing 
// each string of one or more blanks by a single blank.

int main() {
  int c=0;
  int prev_char=0;
  while((c=getchar())!=EOF) {
     if(c==' ' && prev_char==' ') {
       // do nothing
     } else {
       putchar(c); 
     }
     prev_char=c;
  }
  return 0;
}
