#include <stdio.h>

#define MAXLEN 1000

// Exercise 4-12. Adapt the ideas of printd to write a recursive version of 
// itoa ; that is, convert an integer into a string by calling a recursive 
// routine.
//
int itoa(int x, int pos, char s[]); 

int main() {
  char s[MAXLEN];

  itoa(-1234, 0, s);

  printf("%s\n",s);
  return 0;
}

int itoa(int x, int pos, char s[]) {
  if(x<0) {
    s[pos++]='-';
    x=-x;
  }
  if(x<10) {
    s[pos]=x+'0';
    s[pos+1]=0;
    return pos+1;
  }
  int length=itoa(x/10, pos, s);
  s[length] = (x%10+'0');
  s[length+1]= 0;
  return length+1;
}
