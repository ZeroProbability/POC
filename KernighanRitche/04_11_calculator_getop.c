#include <ctype.h>
#include <stdio.h>

#define NUMBER  0 /* signal that a number was found */

int getch(void);

#define BUFSIZE 100

/* getop: get next character or numeric operand */

int getop(char s[])
{
  int i, c;
  static int buffer=EOF; // if this contains EOF, it is empty

  if(buffer==EOF) {
    c=getch();
  } else {
    c=buffer;
    buffer=EOF;
  }

  s[0]=c;

  while (c == ' ' || c == '\t')
    s[0]=c=getch();
  s[1] = '\0';
  if (!isdigit(c) && c != '.')
    return c;
  /* not a number */
  i = 0;
  if (isdigit(c))
    /* collect integer part */
    while (isdigit(s[++i] = c = getch()))
      ;
  if (c == '.')
    /* collect fraction part */
    while (isdigit(s[++i] = c = getch()))
      ;
  s[i] = '\0';
  if (c != EOF) 
    buffer=c;
  return NUMBER;
}
