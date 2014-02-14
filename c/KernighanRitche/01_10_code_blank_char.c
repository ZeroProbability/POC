#include <stdio.h>

// Exercise 1-10. Write a program to copy its input to its output, replacing 
// each tab by \t , each backspace by \b , and each backslash by \\ . This 
// makes tabs and backspaces visible in an unambiguous way.

int main() {
  int c=0;
  while((c=getchar())!=EOF) {
    if(c=='\\') printf("\\\\");
    else if(c=='\b') printf("\\b");
    else if(c=='\t') printf("\\t");
    else putchar(c);
  }
  return 0;
}
