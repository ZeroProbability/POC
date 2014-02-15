#include <stdio.h>

// Exercise 4-1. Write the function strindex(s,t) which returns the position of
// the rightmost occurrence of t in s , or -1 if there is none.
//

int strindex(char s[], char t); 

int main() {
  char *s="some string goes here";
  char c='x';
  printf("rightmost occurance of '%c' in '%s' is %d\n",c,s,strindex(s,c));
  return 0;
}

int strindex(char s[], char t) {
  int i=0,k=-1;
  while(s[i]!=0) {
    if(s[i]==t) k=i;
    i++;
  }
  return k;
}
