#include <stdio.h>
#include <string.h>
#include <limits.h>

#define MAXLENGTH 1000

// Exercise 3-5. Write the function itob(n,s,b) that converts the integer n 
// into a base b character representation in the string s . In particular, 
// itob(n,s,16) formats s as a hexadecimal integer in s .

void itob(int n, char s[], int b);
void reverse(char s[]);
char smod(int n, int b) ;

int main() {
  char s[MAXLENGTH];

  itob(INT_MIN,s,16);
  printf("%s\n",s);
  return 0;
}

char smod(int n, int b) {
  int r=n%b;
  if(r<0) r=-r;
  if(r<10) return '0'+r;
  else return 'a'+(r-10);
}

/* itob: convert n to characters in s */
void itob(int n, char s[], int b)
{
  int i=0, sign;
  if(n==INT_MIN) {
    s[i++]=smod(n,b);
    n=n/b;
  } 
  if ((sign = n) < 0) /* record sign */
    n = -n;
  /* make n positive */
  do {
    /* generate digits in reverse order */
    s[i++] = smod(n,b);/* get next digit */
  } while ((n /= b) > 0);
  /* delete it */
  if (sign < 0)
    s[i++] = '-';
  s[i] = '\0';
  reverse(s);
}

void reverse(char s[]) {
  int len=strlen(s);
  int i,j; char c;
  for(i=0, j=len-1;i<j;i++,j--) {
    c=s[i];
    s[i]=s[j];
    s[j]=c;
  }
}
