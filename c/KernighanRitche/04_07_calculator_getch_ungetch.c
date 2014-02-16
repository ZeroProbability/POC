#include <ctype.h>
#include <stdio.h>
#include <string.h>

#define BUFSIZE 100
char buf[BUFSIZE];
int bufp = 0;

void reverse(char s[]);

/* buffer for ungetch */
/* next free position in buf */
int getch(void) /* get a (possibly pushed-back) character */
{
  return (bufp > 0) ? buf[--bufp] : getchar();
}
void ungetch(int c)
  /* push character back on input */
{
  if (bufp >= BUFSIZE)
    printf("ungetch: too many characters\n");
  else
    buf[bufp++] = c;
}

void ungets(char c[]) {
  int i=0;

  reverse(c);
  while(c[i]!=0) ungetch(c[i++]);
}

void reverse(char c[]) {
  int n=strlen(c);
  int i=0;
  while(i<n/2) {
    char c1=c[i];
    c[i]=c[n-i-1];
    c[n-i-1]=c1;
    i++;
  }
}
