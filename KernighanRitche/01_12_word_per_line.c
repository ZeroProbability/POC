#include <stdio.h>

// Exercise 1-12. Write a program that prints its input one word per line.

int main() {
  int c=0;
  int inside_word=0;
  while((c=getchar())!=EOF) {
     if((c>='a' && c<='z') || (c>='A' && c<='Z') || (c>='0' && c<='9')) {
       inside_word=1;
       putchar(c);
     } else if(inside_word) {
       putchar('\n');
       inside_word=0;
     }
  }
  return 0;
}
