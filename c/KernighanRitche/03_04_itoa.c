#include <stdio.h>

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

void itoa(int n, char s[]);

int main() {
  char s1[MAXLENGTH]="a-z -x-z A-z a-Z -z 9-0 0-8";
  char s2[MAXLENGTH];

  itoa(s1,s2);
  printf("%s\n",s2);
  return 0;
}

/* itoa: convert n to characters in s */
void itoa(int n, char s[])
{
  int i, sign;
  if ((sign = n) < 0) /* record sign */
    n = -n;
  /* make n positive */
  i = 0;
  do {
    /* generate digits in reverse order */
    s[i++] = n % 10 + '0'; /* get next digit */
  } while ((n /= 10) > 0);
  /* delete it */
  if (sign < 0)
    s[i++] = '-';
  s[i] = '\0';
  reverse(s);
}
