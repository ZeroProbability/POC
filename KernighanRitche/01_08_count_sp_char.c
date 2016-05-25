#include <stdio.h>

// Exercise 1-8. Write a program to count blanks, tabs, and newlines.

int main() {
  int c=0;
  int newline_count=0, tab_count=0, blank_count=0;
  while((c=getchar())!=EOF) {
     if(c=='\n') newline_count++;
     if(c=='\t') tab_count++;
     if(c==' ') blank_count++;
  }
  printf("newline: %d, tabs: %d, blanks: %d\n", newline_count, tab_count, blank_count);
  return 0;
}
