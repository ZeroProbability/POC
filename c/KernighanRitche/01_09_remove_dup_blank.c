#include <stdio.h>

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
