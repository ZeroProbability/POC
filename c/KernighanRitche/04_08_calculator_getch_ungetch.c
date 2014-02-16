#include <ctype.h>
#include <stdio.h>

char buf;
int buffer_empty = 1;
/* buffer for ungetch */
/* next free position in buf */
int getch(void) /* get a (possibly pushed-back) character */
{
  if(!buffer_empty) {
    buffer_empty=1;
    return buf;
  }
  return getchar();
}
void ungetch(int c)
  /* push character back on input */
{
  buffer_empty=0;
  buf=c;
}
