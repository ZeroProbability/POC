#include <stdio.h>
#include <string.h>
#include <limits.h>

#define MAXLENGTH 1000 

// Exercise 3-4. In a two's complement number representation, our version of 
// itoa does not handle the largest negative number, that is, the value of n 
// equal to -(2 wordsize-1 ). Explain why not.  Modify it to print that value 
// correctly, regardless of the machine on which it runs.
//
//      void itoa(int n, char s[])
//      {
//        int i, sign;
//        if ((sign = n) < 0) /* record sign */
//          n = -n;
//        /* make n positive */
//        i = 0;
//        do {
//          /* generate digits in reverse order */
//          s[i++] = n % 10 + '0'; /* get next digit */
//        } while ((n /= 10) > 0);
//        /* delete it */
//        if (sign < 0)
//          s[i++] = '-';
//        s[i] = '\0';
//        reverse(s);
//      }

void itoa(int n, char s[],int l);
void reverse(char s[]);

int main() {
  char s[MAXLENGTH];

  itoa(INT_MIN,s,40);
  printf("%s\n",s);
  return 0; 
} 

/* itoa: convert n to characters in s */
void itoa(int n, char s[], int l)
{
  int i=0, sign;
  if(n==INT_MIN) {
    s[i++]=-(n%10)+'0';
    n=n/10;
  } 
  if ((sign = n) < 0) /* record sign */
    n = -n;
  /* make n positive */
  do {
    /* generate digits in reverse order */
    s[i++] = n % 10 + '0'; /* get next digit */
  } while ((n /= 10) > 0);
  /* delete it */
  if (sign < 0)
    s[i++] = '-';
  int k;int padl=l-i;
  for(k=0;k<padl;k++) 
    s[i++]=' ';
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
