#include <stdio.h>

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
