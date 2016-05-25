#include <ctype.h>
#include <stdio.h>

#define BUFSIZE 100
/* buffer for ungetch */
/* next free position in buf */
int getch(void) /* get a (possibly pushed-back) character */
{
  return getchar();
}
