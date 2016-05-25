#include <stdio.h>
#include <string.h>

// Exercise 4-13. Write a recursive version of the function reverse(s) , 
// which reverses the string s in place.
void reverse(char s[],int start, int end) ;

int main() {
  char s[]="some line to be reversed";

  reverse(s, 0, strlen(s)-1);
  printf("%s\n",s);
  
  return 0;
}

void reverse(char s[],int start, int end) {
  if(start>=end) return;
  char c=s[start];
  s[start]=s[end];
  s[end]=c;
  reverse(s,start+1,end-1);
}

