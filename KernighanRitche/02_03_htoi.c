#include <stdio.h>

// Exercise 2-3. Write a function htoi(s) , which converts a string of 
// hexadecimal digits (including an optional 0x or 0X ) into its equivalent 
// integer value. The allowable digits are 0 through 9 , a through f , and 
// A through F .
//
int htoi(char s[]);

int main() {
  printf("%d\n",htoi("0x23a"));
  printf("%d\n",htoi("0xffff"));
  printf("%d\n",htoi("0X111"));
  return 0;
}

int htoi(char s[]) {
  int i=0;
  int out=0;

  if(s[0]=='0' && (s[i]=='x' || s[i]=='X')) i+=2; 
  for(;s[i]!='\0';i++){
    int t=0;
    if(s[i]>='0' && s[i]<='9') {
      t=s[i]-'0';
    } else if(s[i]>='a' && s[i]<='f') {
      t=s[i]-'a'+10;
    } else if(s[i]>='A' && s[i]<='F') {
      t=s[i]-'A'+10;
    } else {
      // TODO: error handling
    }
    out=out*16+t;
  }
  return out;
}
