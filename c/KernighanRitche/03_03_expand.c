#include <stdio.h>

#define MAXLENGTH 1000
// Exercise 3-3. Write a function expand(s1,s2) that expands shorthand 
// notations like a-z in the string s1 into the equivalent complete list 
// abc...xyz in s2 . Allow for letters of either case and digits, and be 
// prepared to handle cases like a-b-c and a-z0-9 and -a-z . Arrange that 
// a leading or trailing - is taken literally.

void expand(char s1[], char s2[]) ;

int main() {
  char s1[MAXLENGTH]="a-z -x-z A-z a-Z -z 9-0 0-8";
  char s2[MAXLENGTH];

  expand(s1,s2);
  printf("%s\n",s2);
  return 0;
}

void expand(char s1[], char s2[]) {
  int i=0,j=0;
  while(s1[i]!=0) {
    if(s1[i+1]=='-') {
      char fc=s1[i];
      char tc=s1[i+2];
      int valid=0;
      if(fc>='a' && fc<='z' && tc>='a' && tc<='z' && fc <= tc) valid=1;
      if(fc>='A' && fc<='Z' && tc>='A' && tc<='Z' && fc <= tc) valid=1;
      if(fc>='0' && fc<='9' && tc>='0' && tc<='9' && fc <= tc) valid=1;
      if(valid==1) {
        char c;
        for(c=fc;c<=tc;c++) {
          s2[j++]=c;
        }
        i+=2;
      } else {
        s2[j++]=fc;
      }
    } else {
      s2[j++]=s1[i];
    }
    i++;
  }
  s2[j]=0;
}
